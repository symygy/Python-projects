import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from kalkulator import Ui_MainWindow

class Kalkulator(Ui_MainWindow):
    numery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    buttons = ['pb0', "pb1"]

    def __init__(self, calc):
        Ui_MainWindow.__init__(self)
        self.setupUi(calc)

        #buttons connections


        self.pb0.clicked.connect(lambda: self.wyswietl("0"))
        self.pb1.clicked.connect(lambda: self.wyswietl("1"))
        self.pb2.clicked.connect(lambda: self.wyswietl("2"))
        self.pb3.clicked.connect(lambda: self.wyswietl("3"))
        self.pb4.clicked.connect(lambda: self.wyswietl("4"))
        self.pb5.clicked.connect(lambda: self.wyswietl("5"))
        self.pb6.clicked.connect(lambda: self.wyswietl("6"))
        self.pb7.clicked.connect(lambda: self.wyswietl("7"))
        self.pb8.clicked.connect(lambda: self.wyswietl("8"))
        self.pb9.clicked.connect(lambda: self.wyswietl("9"))
        self.pbKropka.clicked.connect(lambda: self.wyswietl("."))
        self.pbClear.clicked.connect(lambda: self.leWyswietlacz.setText(""))

        self.pbDodaj.clicked.connect(lambda: self.wyswietl(" + "))
        self.pbOdejmij.clicked.connect(lambda: self.wyswietl(" - "))
        self.pbMnozenie.clicked.connect(lambda: self.wyswietl(" * "))
        self.pbDzielenie.clicked.connect(lambda: self.wyswietl(" / "))
        self.pbWynik.clicked.connect(self.oblicz)

    #definicje metod
    def wyswietl(self, txt):
        self.leWyswietlacz.insert(txt)

    def oblicz(self):
        screen_value = (self.leWyswietlacz.text()).split(' ') #split wpisuje do tablicy elementy ktore sa odzielone spacja

        val1 = float(screen_value[0])
        operator = screen_value[1]
        val2 = float(screen_value[2])
        wynik = self.obliczenia(val1, operator, val2)
        self.leWyswietlacz.setText(str(wynik))

    def obliczenia(self, val1, operator, val2):
        val1 = float(val1)
        val2 = float(val2)

        if operator == '+':
            return val1 + val2
        elif operator == '-':
            return val1 - val2
        elif operator == '*':
            return val1 * val2
        elif operator == '/':
            return val1 / val2





if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    calc=QtWidgets.QMainWindow()
    prog = Kalkulator(calc)
    calc.show()
    sys.exit(app.exec())