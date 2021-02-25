import os
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox
import sys
import Ui_qr_scaner
import time
from pdf2image import convert_from_path
from pyzbar.pyzbar import decode
from PIL import Image


class App(QMainWindow, Ui_qr_scaner.Ui_MainWindow):
    zaman = time.time()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_select.clicked.connect(self.selectFolder)
        self.btn_open.clicked.connect(self.openFolder)
        self.btn_cancel.clicked.connect(self.cancalled)
        self.btn_start.clicked.connect(self.startProcess)

    def selectFolder(self):
        self.yol = QFileDialog.getExistingDirectory(self, 'Klasor Seciniz...')
        print(self.yol)
        if self.yol != (''):
            self.lineEdit.setText(self.yol)
            self.btn_cancel.setEnabled(True)
            self.btn_open.setEnabled(True)
            self.btn_start.setEnabled(True)
        else:
            QMessageBox.warning(self, 'Uyarı', 'Klasör seçimi yapmadınız..!')
            self.lineEdit.setText('')
            self.btn_start.setEnabled(False)
            return

    def openFolder(self):
        path = os.path.realpath(self.yol)
        os.startfile(path)

    def cancalled(self):
        self.lineEdit.setText("")
        self.btn_open.setEnabled(False)
        self.btn_start.setEnabled(False)

    def startProcess(self):
        sayac = 0
        value = 0
        progress = 0
        os.chdir(self.yol)
        dosyalar = os.listdir(self.yol)
        for dosya in dosyalar:
            value += 1

        for dosya in dosyalar:
            sayac += 1
            progress += 100/value
            self.label_kalan.setText(
                "Biten:"+str(sayac)+" // Toplam Adet:" + str(value))
            self.convertImg(dosya)
            dname = str(self.docname)
            dname = dname.split("_")
            dname = dname[0]+".pdf"
            os.rename(dosya, dname)
            if (progress > 99):
                self.progressBar.setValue(100)
            else:
                self.progressBar.setValue(int(progress))
            # print(str(progress))
        if (sayac == 0):
            QMessageBox.warning(self, 'Uyarı', 'Dosya bulunamadı..!')
            return
        QMessageBox.information(self, 'Bilgi', str(
            sayac)+' Adet dosya isimlendirildi..!')
        self.btn_start.setEnabled(False)
        self.label_zaman.setText("Toplam Geçen Süre:" + str(round(time.time()-self.zaman))+"sn"
                                 + " // Dosya Başına:" + str(round(time.time()-self.zaman)/sayac)+"sn")
        # print(str(time.time()-self.zaman))

    def convertImg(self, file):
        outputDir = "C:/temp/"
        if not os.path.exists(outputDir):
            os.makedirs(outputDir)

        pages = convert_from_path(file, 200)
        #counter = 1

        # for page in pages:
        myfile = outputDir + 'output' + str(self.zaman) + '.jpg'
        #counter = counter + 1
        pages[0].save(myfile, "JPEG")
        self.qrRead(myfile)
        # print(myfile)

    def qrRead(self, file):
        self.docname=""
        try:
            d = decode(Image.open(file))
            self.docname = d[0].data.decode('ascii')
        except IndexError:
            return
            #print(self.docname)


app = QApplication(sys.argv)
pencere = App()
pencere.show()
sys.exit(app.exec_())
