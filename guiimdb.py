# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(682, 669)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 511, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.wpiszEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.wpiszEdit.setGeometry(QtCore.QRect(10, 50, 311, 20))
        self.wpiszEdit.setObjectName("wpiszEdit")
        self.SzukajBtn = QtWidgets.QPushButton(self.centralwidget)
        self.SzukajBtn.setGeometry(QtCore.QRect(340, 50, 331, 23))
        self.SzukajBtn.setObjectName("SzukajBtn")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 90, 311, 521))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.lbl1 = QtWidgets.QLabel(self.groupBox)
        self.lbl1.setGeometry(QtCore.QRect(10, 30, 51, 21))
        self.lbl1.setObjectName("lbl1")
        self.rokLbl = QtWidgets.QLabel(self.groupBox)
        self.rokLbl.setGeometry(QtCore.QRect(10, 60, 51, 21))
        self.rokLbl.setObjectName("rokLbl")
        self.krajLbl = QtWidgets.QLabel(self.groupBox)
        self.krajLbl.setGeometry(QtCore.QRect(10, 90, 51, 21))
        self.krajLbl.setObjectName("krajLbl")
        self.tytulEdit = QtWidgets.QLineEdit(self.groupBox)
        self.tytulEdit.setGeometry(QtCore.QRect(90, 30, 211, 20))
        self.tytulEdit.setReadOnly(True)
        self.tytulEdit.setObjectName("tytulEdit")
        self.rokEdit = QtWidgets.QLineEdit(self.groupBox)
        self.rokEdit.setGeometry(QtCore.QRect(90, 60, 211, 20))
        self.rokEdit.setReadOnly(True)
        self.rokEdit.setObjectName("rokEdit")
        self.krajEdit = QtWidgets.QLineEdit(self.groupBox)
        self.krajEdit.setGeometry(QtCore.QRect(90, 90, 211, 20))
        self.krajEdit.setReadOnly(True)
        self.krajEdit.setObjectName("krajEdit")
        self.krajLbl_2 = QtWidgets.QLabel(self.groupBox)
        self.krajLbl_2.setGeometry(QtCore.QRect(10, 120, 71, 21))
        self.krajLbl_2.setObjectName("krajLbl_2")
        self.premieraEdit = QtWidgets.QLineEdit(self.groupBox)
        self.premieraEdit.setGeometry(QtCore.QRect(90, 120, 211, 20))
        self.premieraEdit.setReadOnly(True)
        self.premieraEdit.setObjectName("premieraEdit")
        self.krajLbl_3 = QtWidgets.QLabel(self.groupBox)
        self.krajLbl_3.setGeometry(QtCore.QRect(10, 150, 71, 21))
        self.krajLbl_3.setObjectName("krajLbl_3")
        self.dlugoscEdit = QtWidgets.QLineEdit(self.groupBox)
        self.dlugoscEdit.setGeometry(QtCore.QRect(90, 150, 211, 20))
        self.dlugoscEdit.setReadOnly(True)
        self.dlugoscEdit.setObjectName("dlugoscEdit")
        self.krajLbl_4 = QtWidgets.QLabel(self.groupBox)
        self.krajLbl_4.setGeometry(QtCore.QRect(10, 180, 71, 21))
        self.krajLbl_4.setObjectName("krajLbl_4")
        self.ocenaEdit = QtWidgets.QLineEdit(self.groupBox)
        self.ocenaEdit.setGeometry(QtCore.QRect(90, 180, 211, 20))
        self.ocenaEdit.setReadOnly(True)
        self.ocenaEdit.setObjectName("ocenaEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setGeometry(QtCore.QRect(10, 270, 291, 231))
        self.textBrowser.setObjectName("textBrowser")
        self.krajLbl_5 = QtWidgets.QLabel(self.groupBox)
        self.krajLbl_5.setGeometry(QtCore.QRect(10, 250, 71, 21))
        self.krajLbl_5.setObjectName("krajLbl_5")
        self.glosyEdit = QtWidgets.QLineEdit(self.groupBox)
        self.glosyEdit.setGeometry(QtCore.QRect(110, 210, 191, 20))
        self.glosyEdit.setReadOnly(True)
        self.glosyEdit.setObjectName("glosyEdit")
        self.krajLbl_6 = QtWidgets.QLabel(self.groupBox)
        self.krajLbl_6.setGeometry(QtCore.QRect(10, 210, 101, 21))
        self.krajLbl_6.setObjectName("krajLbl_6")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(340, 90, 331, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(80, 20, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(80, 50, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.ocenaLblIMDB = QtWidgets.QLabel(self.groupBox_2)
        self.ocenaLblIMDB.setGeometry(QtCore.QRect(180, 30, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ocenaLblIMDB.setFont(font)
        self.ocenaLblIMDB.setObjectName("ocenaLblIMDB")
        self.ocenaLblFW = QtWidgets.QLabel(self.groupBox_2)
        self.ocenaLblFW.setGeometry(QtCore.QRect(180, 60, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ocenaLblFW.setFont(font)
        self.ocenaLblFW.setObjectName("ocenaLblFW")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(340, 190, 331, 241))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 311, 211))
        self.listWidget.setObjectName("listWidget")
        self.zapiszBazaBtn = QtWidgets.QPushButton(self.centralwidget)
        self.zapiszBazaBtn.setGeometry(QtCore.QRect(340, 440, 111, 23))
        self.zapiszBazaBtn.setObjectName("zapiszBazaBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 682, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionZapisz_do_pliku = QtWidgets.QAction(MainWindow)
        self.actionZapisz_do_pliku.setObjectName("actionZapisz_do_pliku")
        self.actionZapisz_plakat = QtWidgets.QAction(MainWindow)
        self.actionZapisz_plakat.setObjectName("actionZapisz_plakat")
        self.actionZako_cz = QtWidgets.QAction(MainWindow)
        self.actionZako_cz.setObjectName("actionZako_cz")
        self.menuMenu.addAction(self.actionZapisz_do_pliku)
        self.menuMenu.addAction(self.actionZapisz_plakat)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionZako_cz)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Wpisz tytuł filmu, który chcesz wyszukać:"))
        self.SzukajBtn.setText(_translate("MainWindow", "Szukaj !"))
        self.groupBox.setTitle(_translate("MainWindow", "Dane o filmie:"))
        self.lbl1.setText(_translate("MainWindow", "Tytuł:"))
        self.rokLbl.setText(_translate("MainWindow", "Rok:"))
        self.krajLbl.setText(_translate("MainWindow", "Kraj:"))
        self.krajLbl_2.setText(_translate("MainWindow", "Premiera:"))
        self.krajLbl_3.setText(_translate("MainWindow", "Długość:"))
        self.krajLbl_4.setText(_translate("MainWindow", "Ocena:"))
        self.krajLbl_5.setText(_translate("MainWindow", "Opis:"))
        self.krajLbl_6.setText(_translate("MainWindow", "Ilość głosów:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Ocena:"))
        self.label_2.setText(_translate("MainWindow", "IMDB:"))
        self.label_3.setText(_translate("MainWindow", "Filmweb:"))
        self.ocenaLblIMDB.setText(_translate("MainWindow", "brak oceny"))
        self.ocenaLblFW.setText(_translate("MainWindow", "brak oceny"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Ostatnio wyszukiwane:"))
        self.zapiszBazaBtn.setText(_translate("MainWindow", "Zapisz do bazy"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionZapisz_do_pliku.setText(_translate("MainWindow", "Zapisz do pliku..."))
        self.actionZapisz_plakat.setText(_translate("MainWindow", "Zapisz plakat"))
        self.actionZako_cz.setText(_translate("MainWindow", "Zakończ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

