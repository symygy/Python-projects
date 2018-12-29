
from __future__ import unicode_literals
from ksztalty import Ksztalty, Ksztalt
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QCheckBox, QButtonGroup, QVBoxLayout


class Ui_Widget(object):
    """ Klasa definiująca GUI """

    def setupUi(self, Widget):

        # widget rysujący kształty, instancja klasy Ksztalt
        self.ksztalt = Ksztalt(self, Ksztalty.Polygon)

        # układ poziomy, zawiera: self.ksztalt
        ukladH1 = QHBoxLayout()
        ukladH1.addWidget(self.ksztalt)

        self.setLayout(ukladH1)  # przypisanie układu do okna głównego
        self.setWindowTitle('Widżety')

        #widgety rysujace ksztalty, instancje klasy Ksztalt
        self.ksztalt1 = Ksztalt(self, Ksztalty.Polygon)
        self.ksztalt2 = Ksztalt(self, Ksztalty.Ellipse)
        self.ksztaltAktywny = self.ksztalt1

        #przyciski checkbox
        uklad = QVBoxLayout() # uklad pionowy
        self.grupaChk = QButtonGroup()
        for i, v in enumerate (('Kwadrat', 'Kolo', 'Trojkat', 'Linia')): #odczytuje z tupli kolejne indeksy i etykiety przyciskow
            self.chk = QCheckBox(v) #odczytane etykiety przekazujemy do konstruktora
            self.grupaChk.addButton(self.chk, i) #w danym momencie powienien byc aktywny tylko jeden przycisk. Do klasy QButtonGroup dodajemy przyciski oznaczajac je kolejnymi indeksami
            uklad.addWidget(self.chk)

        self.grupaChk.buttons()[self.ksztaltAktywny.ksztalt].setChecked(True) #zaznacza przycisk ktory odpowiada aktualnemu ksztaltowi

        #checkboxc do wyboru aktywnego ksztaltu
        self.ksztaltChk = QCheckBox('<=')
        self.ksztaltChk.setChecked(True)
        uklad.addWidget(self.ksztaltChk)

        #uklad poziomy dla ksztaltow oraz przyciskow checkbox
        ukladH1 = QHBoxLayout()
        ukladH1.addWidget(self.ksztalt1)
        ukladH1.addLayout(uklad)
        ukladH1.addWidget(self.ksztalt2)

        self.setLayout(ukladH1) #przypisanie ukladu do glownego okna
        self.setWindowTitle("Widgety")
