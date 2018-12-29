import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from gui2 import Ui_MainWindow

class MyGUI(Ui_MainWindow):
    def __init__(self, MainWindow):
        loadUi('test1.ui', self)

        self.pbZamien.clicked.connect(self.lineWpisz.clear)








if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
