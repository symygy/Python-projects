# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1.ui'
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
        self.btnWpisz = QtWidgets.QPushButton(self.centralwidget)
        self.btnWpisz.setGeometry(QtCore.QRect(10, 80, 75, 23))
        self.btnWpisz.setObjectName("btnWpisz")
        self.lineWpisz = QtWidgets.QLineEdit(self.centralwidget)
        self.lineWpisz.setGeometry(QtCore.QRect(10, 50, 113, 20))
        self.lineWpisz.setObjectName("lineWpisz")
        self.listLista = QtWidgets.QListWidget(self.centralwidget)
        self.listLista.setGeometry(QtCore.QRect(150, 10, 256, 192))
        self.listLista.setObjectName("listLista")
        self.pbZamien = QtWidgets.QPushButton(self.centralwidget)
        self.pbZamien.setGeometry(QtCore.QRect(50, 280, 75, 23))
        self.pbZamien.setObjectName("pbZamien")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuZamknij = QtWidgets.QMenu(self.menubar)
        self.menuZamknij.setObjectName("menuZamknij")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuZamknij.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnWpisz.setText(_translate("MainWindow", "Wpisz do listy"))
        self.pbZamien.setText(_translate("MainWindow", "PushButton"))
        self.menuZamknij.setTitle(_translate("MainWindow", "Zamknij"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

