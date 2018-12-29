# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 160, 71, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 180, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuOpcje = QtWidgets.QMenu(self.menubar)
        self.menuOpcje.setObjectName("menuOpcje")
        self.menuNumer_1 = QtWidgets.QMenu(self.menuOpcje)
        self.menuNumer_1.setObjectName("menuNumer_1")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNumer_2 = QtWidgets.QAction(MainWindow)
        self.actionNumer_2.setObjectName("actionNumer_2")
        self.actionWybierz = QtWidgets.QAction(MainWindow)
        self.actionWybierz.setObjectName("actionWybierz")
        self.menuNumer_1.addAction(self.actionWybierz)
        self.menuOpcje.addAction(self.menuNumer_1.menuAction())
        self.menuOpcje.addAction(self.actionNumer_2)
        self.menuOpcje.addSeparator()
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuOpcje.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.menubar.close)
        self.pushButton_2.clicked.connect(self.menubar.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Ukryj menu"))
        self.pushButton_2.setText(_translate("MainWindow", "Pokaz menu"))
        self.menuMenu.setTitle(_translate("MainWindow", "menu"))
        self.menuOpcje.setTitle(_translate("MainWindow", "opcje"))
        self.menuNumer_1.setTitle(_translate("MainWindow", "numer 1"))
        self.actionNumer_2.setText(_translate("MainWindow", "numer 2"))
        self.actionWybierz.setText(_translate("MainWindow", "wybierz"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

