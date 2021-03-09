#coded by oguzkaba

import os
import shutil
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox
import sys
import Ui_qr_scaner
import time
from pdf2image import convert_from_path
from pyzbar.pyzbar import decode
from PIL import Image
import PyPDF2
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
        #print(self.yol)
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
                #print("sayac: "+str(sayac))
                progress += 100/value
                self.label_kalan.setText(
                    "Biten:"+str(sayac)+" // Toplam Adet:" + str(value))
                self.convertImg(dosya)
                if self.docname != "":
                    dname = str(self.docname)+".pdf"
                    if os.path.exists(dname):
                        QMessageBox.warning(self, 'Uyarı',
                                            'Aynı isimde dosya var\nDaha önce isimlendirilmiş olabilir..!')
                        log = open(self.yol+"/log.txt", "a")
                        log.write(
                dosya.ljust(50,"-") + ' -> Aynı isimde dosya var,daha önce isimlendirilmiş olabilir..!\n')                    
                    else:
                        os.rename(dosya, dname)
                self.progressBar.setValue(int(progress))
        if (sayac == 0):
            QMessageBox.warning(self, 'Uyarı', 'Dosya bulunamadı..!')
            return
        self.btn_start.setEnabled(False)
        self.label_zaman.setText("Toplam Geçen Süre:" + str(round(time.time()-self.zaman,2))+"sn"
                                 + " // Dosya Başına:" + str(round(round(time.time()-self.zaman)/sayac,2))+"sn")
        shutil.rmtree("C:/temp/oguz/")
        if (progress > 99) or sayac == value:
            self.progressBar.setValue(100)
        if os.path.exists(self.yol+"/log.txt"):
            self.label_log.setVisible(True)
        # QMessageBox.information(self, 'Bilgi', str(
        #     sayac)+' Adet dosya isimlendirildi..!')
        # print(str(time.time()-self.zaman))
        self.pdfCombine()

    def convertImg(self, file):
        #print("convertImg a gelindi...")
        outputDir = "C:/temp/oguz/"
        if not os.path.exists(outputDir):
            os.makedirs(outputDir)
        pages = convert_from_path(file,int(self.spinBox.text()))     # dpi>200
        #counter = 1
        # for page in pages:
        myfile = outputDir + 'output' + str(self.zaman) + '.jpg'
        #counter = counter + 1
        pages[0].save(myfile, "JPEG")
        #print("convertIMAGE: "+myfile)
        self.qrRead(myfile, file)
        # print(myfile)

    def qrRead(self, file, pdffile):
        #print("qrRead e gelindi...")
        self.docname = ""
        try:
            d = decode(Image.open(file))
            self.docname = d[0].data.decode('ascii')
            #print("qrReade"+self.docname)
        except:
            QMessageBox.warning(self, 'Uyarı', 'QR okunamadı..!\n' + file)
            log = open(self.yol+"/log.txt", "a")
            log.write(
                pdffile.ljust(50,"-")  + ' -> QR okunamadı..!\n')
            #print("qrRead:"+self.docname)
            return
            # print(self.docname)

    def logOpen(self,event):
        os.startfile(self.yol+"/log.txt")

    def pdfCombine(self):
        dosyalar=os.listdir(self.yol)

        for dosya in dosyalar:
            yol1=self.yol+"/"
            pdf_merger = PyPDF2.PdfFileMerger()
            if dosya.endswith('.pdf'):                          #pdf dosyalasımı?                     
                if dosya.count("_")>0 and dosya.count("-"):     #Daha önce isimlendirilmiş mi?
                    docAppendname=[]                            #listeyi sıfırla
                    dosyakisa = dosya.split("_")
                    tekilDosya=dosyakisa[1]
                    ind=tekilDosya.index("-")
                    tekil=len(tekilDosya)-4
                    tekilDosya=tekilDosya[ind+1:tekil]
                    dosyakisa = dosyakisa[0]
                    if tekilDosya=="1":
                        print("Tekil Dosya : "+tekilDosya)
                        os.rename(yol1+dosya,yol1+dosyakisa+".pdf")
                    else:    
                        for i in range(1,len(dosyalar)):
                            dosya2=dosyalar[i]
                            if dosya2.endswith('.pdf'):  
                                dosya2kisa = dosya2.split("_")           
                                dosya2kisa = dosya2kisa[0]
                                if dosya!=dosya2 and dosyakisa==dosya2kisa: #aynı dosya değil ve kısaltılmış isimleri aynı ise
                                    print("DOSYA1: "+dosya)
                                    print("DOSYA2: "+dosya2)
                                    varmi=dosya in docAppendname
                                    if varmi==False:
                                        docAppendname.append(dosya)
                                    docAppendname.append(dosya2) 
                                    docAppendname.sort()  
                                    print(str(docAppendname)) 
                        #print(str(docAppendname))

                        if int(tekilDosya)>len(docAppendname) and 0<len(docAppendname):
                            dockisa=docAppendname[0].split("_")
                            print("Hata Dosya Eksik...."+str(dockisa[0]))  
                        else:
                            for pdf in docAppendname:
                                print("Eklenecek Dosyalar : "+yol1+pdf)
                                pdf_merger.append(yol1+pdf)
                            pdf = pdf.split("_")           
                            pdf = pdf[0]
                            dosyaKontrol=os.path.exists(yol1+pdf+".pdf")
                            if dosyaKontrol:
                                print("Dosya Zaten Var....................................!")
                            else:    
                                print("Oluşturulacak Dosya :"+yol1+pdf)
                                pdf_merger.write(yol1+pdf+".pdf")
                                print("Dosya Oluşturuldu...: "+yol1+pdf)
                                pdf_merger.close()    
                            for pdf in docAppendname:
                                print(yol1+pdf)
                                os.remove(yol1+pdf)
                                dosyalar.remove(pdf)
                                print("SiLİNDİ... : "+yol1+pdf) 
                            dosyalar=os.listdir(self.yol)
                            print("Dosyalar Listesi : "+str(dosyalar))
                            
                
        

app = QApplication(sys.argv)
pencere = App()
pencere.show()
sys.exit(app.exec_())
