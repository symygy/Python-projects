import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from firstgui import Ui_MainWindow







if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    prog = MyGUI(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())