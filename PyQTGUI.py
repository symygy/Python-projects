import sys
from PyQt5 import QtWidgets

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    b = QtWidgets.QPushButton("Push me !")
    l = QtWidgets.QLabel("This is a lavbel")

    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(l)
    h_box.addStretch()

    v_box = QtWidgets.QVBoxLayout()
    v_box.addWidget(b)
    v_box.addWidget(l)
    v_box.addLayout(h_box)
    w.setLayout(v_box)

    w.setWindowTitle("Lekcja !")
    w.show()

    sys.exit(app.exec_())

window()