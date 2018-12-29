import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from listownik import Ui_Dialog

class MyFirstGuiProgram(Ui_Dialog):
    def __init__(self, dialog):
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)

        # Connect "add" button with a custom function (addInputTextToListbox)
        self.addBtn.clicked.connect(self.addInputTextToListbox)
        self.addBtn2.clicked.connect(self.addInputTextToListbox2)

    def addInputTextToListbox(self):
        txt = self.myTextInput.text()
        self.listWidget.addItem(txt)

    def addInputTextToListbox2(self):
        txt = self.myTextInput2.text()
        self.listWidget2.addItem(txt)


if __name__ == '__main__':

    # Every PyQt5 application must create an application object. The sys.argv parameter is a list of arguments from a command line. Python scripts can be run from the shell. It is a way how we can control the startup of our scripts.
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    prog = MyFirstGuiProgram(dialog)
    dialog.show()
    sys.exit(app.exec_())

