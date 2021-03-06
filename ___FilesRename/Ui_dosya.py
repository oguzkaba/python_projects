# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Oğuz KABA\Desktop\python_projects\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
 
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon('icon.ico'))
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        width=449
        height=309
        MainWindow.setFixedSize(width, height)
        #MainWindow.resize(449, 309)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(5, 5, 441, 301))
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 420, 60))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.klasorSec = QtWidgets.QToolButton(self.groupBox)
        self.klasorSec.setGeometry(QtCore.QRect(390, 30, 25, 22))
        self.klasorSec.setObjectName("klasorSec")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(3, 30, 381, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setInputMask("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 80, 420, 80))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(120, 50, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(370, 30, 31, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(250, 30, 101, 16))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox.setGeometry(QtCore.QRect(370, 50, 42, 22))
        self.spinBox.setMinimum(3)
        self.spinBox.setMaximum(6)
        self.spinBox.setProperty("value", 4)
        self.spinBox.setObjectName("spinBox")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setValidator(QtGui.QIntValidator())
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 50, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(120, 30, 81, 16))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(10, 50, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem(".pdf")
        self.comboBox.addItem(".txt")
        self.comboBox.addItem(".xlsx")
        self.comboBox.addItem(".docx")
        self.comboBox.addItem(".bmp")
        self.comboBox.addItem(".png")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 170, 420, 71))
        self.groupBox_3.setObjectName("groupBox_3")
        self.baslat = QtWidgets.QPushButton(self.groupBox_3)
        self.baslat.setGeometry(QtCore.QRect(130, 30, 75, 30))
        self.baslat.setObjectName("baslat")
        self.baslat.setEnabled(False)
        self.baslat.setStyleSheet("color:rgb(62, 167, 30)")
        self.temizle = QtWidgets.QPushButton(self.groupBox_3)
        self.temizle.setGeometry(QtCore.QRect(210, 30, 75, 30))
        self.temizle.setObjectName("temizle")
        self.cikisYap = QtWidgets.QPushButton(self.groupBox_3)
        self.cikisYap.setGeometry(QtCore.QRect(335, 30, 75, 30))
        self.cikisYap.setObjectName("cikisYap")
        self.klasorAc = QtWidgets.QPushButton(self.groupBox_3)
        self.klasorAc.setGeometry(QtCore.QRect(10, 30, 75, 30))
        self.klasorAc.setObjectName("klasorAc")
        self.klasorAc.setEnabled(False)
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(10, 250, 420, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.listView = QtWidgets.QListWidget(self.tab_2)
        self.listView.setGeometry(QtCore.QRect(7, 5, 421, 250))
        self.listView.setObjectName("listView")
        font1 = QtGui.QFont()
        font1.setPointSize(7)
        self.listView.setFont(font1)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(10, 260, 80, 13))
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dosya Isimlendirme"))
        self.groupBox.setTitle(_translate("MainWindow", "Hedef Klasör Bilgileri"))
        self.klasorSec.setText(_translate("MainWindow", "..."))
        self.lineEdit_3.setText(_translate("MainWindow", "Kaynak seçiniz"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Raporlama Bilgileri"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>Hane</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>Başlangıç No</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Rapor Adı</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>Adet : </p></body></html>"))
        self.comboBox.setPlaceholderText(_translate("MainWindow", "Seçiniz"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Uzanti Seçimi</p></body></html>"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Yapılacak İşlem"))
        self.baslat.setText(_translate("MainWindow", "Başlat"))
        self.temizle.setText(_translate("MainWindow", "Temizle"))
        self.cikisYap.setText(_translate("MainWindow", "Çıkış"))
        self.klasorAc.setText(_translate("MainWindow", "Klasörü Aç"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Rename"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "View Files"))
        