# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listownik.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(818, 384)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(80, 270, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.addBtn = QtWidgets.QPushButton(Dialog)
        self.addBtn.setGeometry(QtCore.QRect(30, 20, 75, 23))
        self.addBtn.setObjectName("addBtn")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(0, 50, 256, 192))
        self.listWidget.setObjectName("listWidget")
        self.myTextInput = QtWidgets.QLineEdit(Dialog)
        self.myTextInput.setGeometry(QtCore.QRect(130, 20, 113, 20))
        self.myTextInput.setObjectName("myTextInput")
        self.addBtn2 = QtWidgets.QPushButton(Dialog)
        self.addBtn2.setGeometry(QtCore.QRect(310, 20, 75, 23))
        self.addBtn2.setObjectName("addBtn2")
        self.myTextInput2 = QtWidgets.QLineEdit(Dialog)
        self.myTextInput2.setGeometry(QtCore.QRect(410, 20, 113, 20))
        self.myTextInput2.setObjectName("myTextInput2")
        self.listWidget2 = QtWidgets.QListWidget(Dialog)
        self.listWidget2.setGeometry(QtCore.QRect(280, 50, 256, 192))
        self.listWidget2.setObjectName("listWidget2")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.addBtn.setText(_translate("Dialog", "Add"))
        self.myTextInput.setPlaceholderText(_translate("Dialog", "dajesz kurwa"))
        self.addBtn2.setText(_translate("Dialog", "Add"))
        self.myTextInput2.setPlaceholderText(_translate("Dialog", "dajesz kurwa"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

