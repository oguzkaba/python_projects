import PyPDF2
import os

# bir="C:/Users/Oğuz KABA/Desktop/_QMS Dosyalar/pdf deneme/a1.pdf"
# iki="C:/Users/Oğuz KABA/Desktop/_QMS Dosyalar/pdf deneme/a2.pdf"

# def pdfbirlestir(bir, iki):
#     print("fonksiyon start...")
#     pdf_merger = PyPDF2.PdfFileMerger()
#     for file in [bir, iki]:
#         pdf_merger.append(file)
#     pdf_merger.write("C:/Users/Oğuz KABA/Desktop/_QMS Dosyalar/pdf deneme/sonuc.pdf")
#     pdf_merger.close()

# pdfbirlestir(bir,iki)    
yol="C:/Users/Oğuz KABA/Desktop/_QMS Dosyalar/pdf deneme/"

def pdfAppend(yol):
    docAppendname=[]
    dosyalar = os.listdir(yol)
    merger = PyPDF2.PdfFileMerger()
    for dosya in dosyalar:
        if dosya.endswith('.pdf'):
            print("DOSYA :"+dosya)
            dosya = dosya.split("_")           #sayfa sayısı
            dosya = dosya[0]
            toplamSayfa=1
            sayfa=0
        for pagees in dosyalar:
            if pagees.endswith('.pdf'):
                pagees = pagees.split("_")           #sayfa sayısı
                pagees = pagees[0]
                if pagees==dosya:
                    sayfa+=1
                    #print("KONTROL :"+yol+"{}_{}-{}.pdf".format(pagees,sayfa,toplamSayfa))
                    # pdf_merger.append(yol+"{}_{}-{}.pdf".format(pagees,sayfa,toplamSayfa))
                    # pdf_merger.write("C:/Users/Oğuz KABA/Desktop/_QMS Dosyalar/pdf deneme/sonuc.pdf")
                    # pdf_merger.close()
                    #print("Sayfa :"+str(sayfa))
            toplamSayfa=sayfa
            ss=0
    for pageess in dosyalar:
        if pageess.endswith('.pdf'):
            pageess = pageess.split("_")           #sayfa sayısı
            pageess = pageess[0]
            if pageess==dosya:
                ss+=1
            #print("KONTROL :"+yol+"{}_{}-{}.pdf".format(pageess,ss,toplamSayfa))
            docAppendname.append(yol+"{}_{}-{}.pdf".format(pageess,ss,toplamSayfa))
            # pdf_merger.append(yol+"{}_{}-{}.pdf".format(pageess,ss,toplamSayfa))
            # pdf_merger.write("C:/Users/Oğuz KABA/Desktop/_QMS Dosyalar/pdf deneme/sonuc.pdf")
            print("SON :"+str(docAppendname))   
    # for pdf in docAppendname:
    #     merger.append(pdf)
    #     pdf = pdf.split("_")           #sayfa sayısı
    #     pdf = pdf[0]
    # merger.write("C:/Users/Oğuz KABA/Desktop/_QMS Dosyalar/pdf deneme/{}.pdf".format(pdf))
    # merger.close()    
    # for pdf in docAppendname:
    #     os.remove(pdf)        
                        
pdfAppend(yol)