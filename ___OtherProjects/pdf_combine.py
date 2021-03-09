import PyPDF2
import os

yol="C:/Users/Oğuz KABA/Desktop/_QMS Dosyalar/pdf deneme/"

dosyalar=os.listdir(yol)

for dosya in dosyalar:
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
                os.rename(yol+dosya,yol+dosyakisa+".pdf")
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
                        print("Eklenecek Dosyalar : "+yol+pdf)
                        pdf_merger.append(yol+pdf)
                    pdf = pdf.split("_")           
                    pdf = pdf[0]
                    dosyaKontrol=os.path.exists(yol+pdf+".pdf")
                    if dosyaKontrol:
                        print("Dosya Zaten Var....................................!")
                    else:    
                        print("Oluşturulacak Dosya :"+yol+pdf)
                        pdf_merger.write(yol+pdf+".pdf")
                        print("Dosya Oluşturuldu...: "+yol+pdf)
                        pdf_merger.close()    
                    for pdf in docAppendname:
                        print(yol+pdf)
                        os.remove(yol+pdf)
                        dosyalar.remove(pdf)
                        print("SiLİNDİ... : "+yol+pdf) 
                    dosyalar=os.listdir(yol)
                    print("Dosyalar Listesi : "+str(dosyalar))
                    
                
        