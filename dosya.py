import os
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox
import sys
import Ui_dosya


class App(QMainWindow, Ui_dosya.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.baslat.clicked.connect(self.startProcess)
        self.klasorSec.clicked.connect(self.selectFolder)
        self.temizle.clicked.connect(self.cleanEntry)
        self.klasorAc.clicked.connect(self.openFolder)
        self.cikisYap.clicked.connect(self.exitApp)

    def selectFolder(self):
        #yolDosya = QFileDialog.getOpenFileName(self, 'Open a file', '','All Files (*.*)')
        self.yol = QFileDialog.getExistingDirectory(self, 'Klasor Seciniz...')
        print(self.yol)
        if self.yol != (''):
            self.lineEdit_3.setText(self.yol)
            self.klasorAc.setEnabled(True)
            self.baslat.setEnabled(True)
        else:
            QMessageBox.warning(self, 'Uyarı', 'Klasör seçimi yapmadınız..!')
            self.lineEdit_3.setText('')
            self.klasorAc.setEnabled(False)

    def openFolder(self):
        path = os.path.realpath(self.yol)
        os.startfile(path)
        print(path)

    def startProcess(self):
        self.uzanti = self.comboBox.currentText()
        rname = self.lineEdit.text()
        self.rapno = self.lineEdit_2.text()

        if (self.uzanti == '' or rname == '' or self.rapno == ''):
            QMessageBox.warning(self, 'Uyarı', 'Boş alan bırakmayınız..!')
        else:
            sayac = 0
            os.chdir(self.yol)
            dosyalar = os.listdir(self.yol)
            self.listView.clear()
            for dosya in dosyalar:
                if dosya.endswith(self.uzanti):
                    sayac = sayac+1
                    self.listView.addItem(dosya)
                    self.label_5.setText('Adet: ' + str(sayac))
                    self.rangeNo()
                    os.rename(dosya, rname+self.rapno+self.uzanti)
                    self.rapno=str(int(self.rapno)+1)
            if (sayac == 0):
                QMessageBox.warning(self, 'Uyarı', 'Dosya bulunamadı..!')
        QMessageBox.information(self, 'Bilgi', str(sayac)+' Adet dosya isimlendirildi..!')        
        self.baslat.setEnabled(False)

    def cleanEntry(self):
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.baslat.setEnabled(False)


    def rangeNo(self):
        rangeNum = self.spinBox.text()
        if (rangeNum == '3'):
            if (int(self.rapno)<10):
                self.rapno = '00'+ self.rapno
            elif (int(self.rapno)<100): 
                self.rapno = '0'+ self.rapno
            else:
                QMessageBox.warning(self, 'Uyarı', 'Aralıktan büyük veya negatif değer girildi..!')
        if (rangeNum == '4'):
            if (int(self.rapno)<10):
                self.rapno = '000'+ self.rapno
            elif (int(self.rapno)<100): 
                self.rapno = '00'+ self.rapno
            elif (int(self.rapno)<1000):
                self.rapno = '0'+ self.rapno    
            else:
                QMessageBox.warning(self, 'Uyarı', 'Aralıktan büyük veya negatif değer girildi..!')      
        elif (rangeNum == '5'):
            if (int(self.rapno)<10):
                self.rapno = '0000'+ self.rapno
            elif (int(self.rapno)<100): 
                self.rapno = '000'+ self.rapno
            elif (int(self.rapno)<1000):
                self.rapno = '00'+ self.rapno 
            elif (int(self.rapno)<10000):
                self.rapno = '0'+ self.rapno  
            else:
                QMessageBox.warning(self, 'Uyarı', 'Aralıktan büyük veya negatif değer girildi..!')       
        elif (rangeNum == '6'):    
            if (int(self.rapno)<10):
                self.rapno = '00000'+ self.rapno
            elif (int(self.rapno)<100): 
                self.rapno = '0000'+ self.rapno
            elif (int(self.rapno)<1000):
                self.rapno = '000'+ self.rapno 
            elif (int(self.rapno)<10000):
                self.rapno = '00'+ self.rapno
            elif (int(self.rapno)<100000):
                self.rapno = '0'+ self.rapno            
            else:
                QMessageBox.warning(self, 'Uyarı', 'Aralıktan büyük veya negatif değer girildi..!')    
        print(self.rapno) 
        return self.rapno  

    def exitApp(self):
        sys.exit()


app = QApplication(sys.argv)
pencere = App()
pencere.show()
sys.exit(app.exec_())
