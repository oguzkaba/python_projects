import os
import shutil
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox
import sys
import Ui_qr_scaner
import time
from pdf2image import convert_from_path
from pyzbar.pyzbar import decode
from PIL import Image


class App(QMainWindow, Ui_qr_scaner.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_select.clicked.connect(self.selectFolder)
        self.btn_open.clicked.connect(self.openFolder)
        self.btn_cancel.clicked.connect(self.cancalled)
        self.btn_start.clicked.connect(self.startProcess)
        self.label_log.mousePressEvent=self.logOpen

    def selectFolder(self):
        self.yol = QFileDialog.getExistingDirectory(self, 'Klasor Seciniz...')
        print(self.yol)
        if self.yol != (''):
            self.lineEdit.setText(self.yol)
            self.btn_cancel.setEnabled(True)
            self.btn_open.setEnabled(True)
            self.btn_start.setEnabled(True)
            self.spinBox.setEnabled(True)
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
        self.zaman = time.time()
        sayac = 0
        value = 0
        progress = 0
        os.chdir(self.yol)
        dosyalar = os.listdir(self.yol)
        for dosya in dosyalar:
            if dosya.endswith('.pdf'):
                value += 1

        for dosya in dosyalar:
            if dosya.endswith('.pdf'):
                sayac += 1
                print("sayac: "+str(sayac))
                progress += 100/value
                self.label_kalan.setText(
                    "Biten:"+str(sayac)+" // Toplam Adet:" + str(value))
                self.convertImg(dosya)
                if self.docname != "":
                    dname = str(self.docname)
                    dname = dname.split("_")
                    dname = dname[0]+".pdf"
                    if os.path.exists(dname):
                        QMessageBox.warning(self, 'Uyarı',
                                            'Aynı isimde dosya var\nDaha önce isimlendirilmiş olabilir..!')
                        log = open(self.yol+"/log.txt", "a")
                        log.write(
                dosya.ljust(50,"-") + ' -> Aynı isimde dosya var,daha önce isimlendirilmiş olabilir..!\n')                    
                    else:
                        os.rename(dosya, dname)
                if (progress > 99) or sayac == value:
                    self.progressBar.setValue(100)
                else:
                    self.progressBar.setValue(int(progress))
                    # print(str(progress))
        if (sayac == 0):
            QMessageBox.warning(self, 'Uyarı', 'Dosya bulunamadı..!')
            return
        self.btn_start.setEnabled(False)
        self.label_zaman.setText("Toplam Geçen Süre:" + str(round(time.time()-self.zaman))+"sn"
                                 + " // Dosya Başına:" + str(round(time.time()-self.zaman)/sayac)+"sn")
        shutil.rmtree("C:/temp/oguz/")
        if os.path.exists(self.yol+"/log.txt"):
            self.label_log.setVisible(True)
        # QMessageBox.information(self, 'Bilgi', str(
        #     sayac)+' Adet dosya isimlendirildi..!')
        # print(str(time.time()-self.zaman))

    def convertImg(self, file):
        print("convertImg a gelindi...")
        outputDir = "C:/temp/oguz/"
        if not os.path.exists(outputDir):
            os.makedirs(outputDir)
        pages = convert_from_path(file,int(self.spinBox.text()))     # dpi>200
        #counter = 1
        # for page in pages:
        myfile = outputDir + 'output' + str(self.zaman) + '.jpg'
        #counter = counter + 1
        pages[0].save(myfile, "JPEG")
        print("convertIMAGE: "+myfile)
        self.qrRead(myfile, file)
        # print(myfile)

    def qrRead(self, file, pdffile):
        print("qrRead e gelindi...")
        self.docname = ""
        try:
            d = decode(Image.open(file))
            self.docname = d[0].data.decode('ascii')
            print("qrReade"+self.docname)
        except:
            QMessageBox.warning(self, 'Uyarı', 'QR okunamadı..!\n' + file)
            log = open(self.yol+"/log.txt", "a")
            log.write(
                pdffile.ljust(50,"-")  + ' -> QR okunamadı..!\n')
            print("qrRead:"+self.docname)
            return
            # print(self.docname)

    def logOpen(self,event):
        os.startfile(self.yol+"/log.txt")

app = QApplication(sys.argv)
pencere = App()
pencere.show()
sys.exit(app.exec_())
