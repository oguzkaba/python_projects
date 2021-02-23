import os
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox
import sys
import Ui_dosya

# bulunduğu klasör
#print(os.getcwd())

#farklı klasöre geçiş
#os.chdir("C:/Users/Oğuz KABA/Desktop/Diğer Dosyalar")

#klasörde bulunan dosyalar
#print(os.listdir())

#klasör oluşturma
# os.mkdir("aa")

#kasör ismi değştirme
#os.rename("aa","yeniKlasor")

#klasör mü?
#os.path.isdir("/home/sinan")

#doya ismi ver -> olmayandosya.py
#os.path.split("/home/sinan/pythonProject/adventureGame/olmayandosya.py")

#dosyanın adını ve uzantısını ayrı ayrı ver -> ('olmayandosya', '.py')
#os.path.splitext("/home/sinan/pythonProject/adventureGame/olmayandosya.py")

#dosya mı?
#os.path.isfile("/home/sinan/pythonProject/adventureGame/index.py")

#dosya yada klasör var mı?
#os.path.exists("/home")

#dosyayı ilgili program ile açma
#os.startfile('deneme.txt')

#uzantı ismi ile dosya listeleme
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
        
        self.pushButton_4.clicked.connect(self.tiklama)
        self.klasorSec.clicked.connect(self.select)
        

    def tiklama(self):
        print('Merhaba')
        self.klasorSec.setEnabled(False)

    def select(self):
        path = QFileDialog.getOpenFileName(self, 'Open a file', '',
                                     'All Files (*.*)')
        if path != ('', ''):
            self.lineEdit_3.setText(path[0])   
        else:
            QMessageBox.critical(self, "Uyarı", "Klasör seçimi yapmadınız..!")


                

app = QApplication(sys.argv)
pencere = App()
pencere.show()
sys.exit(app.exec_())
