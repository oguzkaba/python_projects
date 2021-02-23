import os
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox
import sys
import Ui_dosya


# bulunduğu klasör
# print(os.getcwd())

# farklı klasöre geçiş
# os.chdir("C:/Users/Oğuz KABA/Desktop/Diğer Dosyalar")

# klasörde bulunan dosyalar
# print(os.listdir())

# klasör oluşturma
# os.mkdir("aa")

# kasör ismi değştirme
# os.rename("aa","yeniKlasor")

# klasör mü?
# os.path.isdir("/home/sinan")

# doya ismi ver -> olmayandosya.py
# os.path.split("/home/sinan/pythonProject/adventureGame/olmayandosya.py")

# dosyanın adını ve uzantısını ayrı ayrı ver -> ('olmayandosya', '.py')
# os.path.splitext("/home/sinan/pythonProject/adventureGame/olmayandosya.py")

# dosya mı?
# os.path.isfile("/home/sinan/pythonProject/adventureGame/index.py")

# dosya yada klasör var mı?
# os.path.exists("/home")

# dosyayı ilgili program ile açma
# os.startfile('deneme.txt')

# uzantı ismi ile dosya listeleme
# uzanti=input('Uzantı ismi (.txt, .xlsx gibi) giriniz ?  :')
# sayac=0
# os.chdir('C:/Users/Oğuz KABA/Desktop/_QMS Dosyalar')
# dosyalar = os.listdir('C:/Users/Oğuz KABA/Desktop/_QMS Dosyalar')
# for dosya in dosyalar:
#      if dosya.endswith(uzanti):
#             sayac=sayac+1 
#             os.rename(dosya,str(sayac)+uzanti)
# print(str(sayac) + ' Adet dosya ismi değiştirildi')

class App(QMainWindow, Ui_dosya.Ui_MainWindow):
    

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cikisYap.clicked.connect(self.exitApp)
        self.klasorSec.clicked.connect(self.selectFolder)
        self.klasorAc.clicked.connect(self.openFolder)
        


    def selectFolder(self):
        #yolDosya = QFileDialog.getOpenFileName(self, 'Open a file', '','All Files (*.*)')
        self.yol=QFileDialog.getExistingDirectory(self,'Klasor Seciniz...')  
        print(self.yol)                                 
        if self.yol != (''):
            self.lineEdit_3.setText(self.yol)
        else:
            QMessageBox.critical(self, "Uyarı", "Klasör seçimi yapmadınız..!")

    def openFolder(self):
        path=self.yol
        os.system(f'start {os.path.realpath(path)}')
        #os.open(self.lineEdit_3.text())

    def exitApp(self):
        sys.exit()

app = QApplication(sys.argv)
pencere = App()
pencere.show()
sys.exit(app.exec_())
