import sys
from PyQt5 import QtWidgets
from mainwindow import Ui_MainWindow # import klasy main window z gui

class GUI(Ui_MainWindow):
    def __init__(self, programik):
        Ui_MainWindow.__init__(self)
        self.setupUi(programik)

        #connects buttons
        self.addBtn.clicked.connect(self.addInputTextToListbox)

    def addInputTextToListbox(self):
        txt = self.myTextInput.text()
        self.listWidget.addItem(txt)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    programik = QtWidgets.QMainWindow()
    apka = GUI(programik)
    programik.show()
    sys.exit(app.exec_())

