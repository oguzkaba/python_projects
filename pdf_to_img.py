from pdf2image import convert_from_path
import os
import sys
import time

zaman = time.time()
outputDir = "imag/"

# file="deneme.pdf"


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
        


# args = sys.argv
# if len(args) > 1:
#     file = args[1]
dosyalar = os.listdir("pdf/")
for dosya in dosyalar:
    #print("pdf/" + dosya)
    file = "pdf/" + dosya
    convert(file, outputDir)
print(str(time.time()-zaman))    