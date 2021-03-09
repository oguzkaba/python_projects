from pdf2image import convert_from_path
import os
import sys
import time

zaman = time.time()
outputDir = "imag/"

file="C:/Users/Oğuz KABA/Desktop/_QMS Dosyalar/pdf deneme/aa.pdf"


def convert(file, outputDir):

    #outputDir = outputDir + str(round(time.time())) + '/'
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    pages = convert_from_path(file, 200)
    counter = 1
    
    for page in pages:
        myfile = outputDir + 'output' + str(counter) + '.jpg'
        counter = counter + 1
        page.save(myfile, "JPEG")
        print(myfile)
        

convert(file, outputDir)
# args = sys.argv
# if len(args) > 1:
#     file = args[1]
# dosyalar = os.listdir("C:/Users/Oğuz KABA/Desktop/_QMS Dosyalar/pdf deneme")
# for dosya in dosyalar:
#     #print("pdf/" + dosya)
#     file = dosya
#     print(file)
#     convert(file, outputDir)
# print(str(time.time()-zaman))    