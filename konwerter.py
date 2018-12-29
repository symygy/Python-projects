from PyQt5 import QtWidgets, uic

def Convert():
    dlg.leWynik.setText(str(float(dlg.leWpisz.text())*1.23))

app=QtWidgets.QApplication([])
dlg=uic.loadUi("konwerter.ui")

#connect
dlg.pbKonwertuj.clicked.connect(Convert)
dlg.leWpisz.returnPressed.connect(Convert)

dlg.show()
app.exec_()