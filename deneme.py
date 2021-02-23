# import tempfile
# import glob
# import argparse
# # import xlrd
# import pandas
# from os.path import join, basename
# from shutil import copyfile
# from pdf2image import convert_from_path
# import pdf2image  # , convert_from_bytes
# from pyzbar.pyzbar import decode
# # from PIL import Image

# def cihan(input_folder, excel_file, output_folder):
#     summary = []
#     # load excel file
#     df = pandas.read_excel(excel_file)
#     df = df[['TaskId', 'ElementCode', 'DocName']]
#     for file in glob.glob(join(input_folder, '*.pdf')):
#         # convert pdf file to png
#         # scan the image and get task ids
#         file_name = basename(file)
#         with tempfile.TemporaryDirectory() as path:
#             images_from_path = convert_from_path(file, output_folder=path)
#             task_ids = []
#             for image in images_from_path:
#                 # decode(Image.open('pyzbar/tests/code128.png'))
#                 decoded = decode(image)
#                 for d in decoded:
#                     print(file_name, d.type, d.data.decode("utf-8"))
#                     task_ids.append(int(d.data))
#         # compute new name from excel file by using task ids
#         new_name = []
#         for task_id in task_ids:
#             i = df.index[df['TaskId'] == task_id].tolist()
#             if len(i) > 1:
#                 raise Exception('TaskId {} is multiple times in excel file!'.format(task_id))
#             new_name.append('{}_{}'.format(df['ElementCode'][i[0]], df['DocName'][i[0]]))
#         new_name = '{}.pdf'.format(','.join(new_name))
#         print('new name: ', new_name)
#         copyfile(file, join(output_folder, new_name))
#         summary.append('{} {}\n'.format(basename(file), new_name))
#     with open(join(output_folder, 'summary.txt'), 'w') as f:
#         f.writelines(summary)


# def get_args():
#     parser = argparse.ArgumentParser(description='Scan pdfs and rename them according to '
#                                                  'data in barcodes they contain.'
#                                                  '\nTested on python 3.6.'
#                                                  '\nRequirements: pip install pdf2image pyzbar image pandas xlrd')
#     parser.add_argument('-i', '--input_folder', required=True, help='Where all pdf files take place.')
#     parser.add_argument('-e', '--excel_file', required=True, help='Path of excel file.')
#     parser.add_argument('-o', '--output_folder', required=True, help='Where to copy new renamed pdf files.')
#     args = parser.parse_args()
#     return args


# if __name__ == '__main__':
#     # ex call:
#     # python cihan.py -i '/home/kenan/PycharmProjects/cihan/pdfs' -e '/home/kenan/PycharmProjects/cihan/Book2.xlsx' -o '/home/kenan/PycharmProjects/cihan/output'
#     args = get_args()
#     cihan(args.input_folder, args.excel_file, args.output_folder)



# file=open('newfile.txt','w',encoding='utf-8')

# for i in range(2,100000,2): 
#     file.write(str(i)+"\n") 
# file.close()

# import math as islemler

# value=dir(islemler)
# print(value)

# result=islemler.sqrt(49)
# print(int(result))

# from math import * #factorial,sqrt vs...modülden belirli fonksiyonları import etme

# def sqrt(x):                #fonksiyon tanımlama
#     print('x : '+str(x))        



from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(388, 360)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(140, 160, 61, 61))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 388, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
    # retranslateUi
