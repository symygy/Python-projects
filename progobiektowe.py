
class Calculator():

#self przechowuje poszczegolna instancje

    def __init__(self):  # definiujemy metode magiczna init - konstruktor
        #print("Wykonuje sie init")
        self.liczba=13 #zmienna dostepna dla instancji
        self.ostatni_wynik = 0
    def __del__(self): #destruktor
        print("Wykonuje sie del")

    def __str__(self): # wykonuje sie gdy klase chcemu przekonwerowac na string
        print("len")


    def dodaj(self, a, b):
        wynik=a+b
        self.ostatni_wynik=wynik
        print(wynik)
    def odejmij(self,a,b):
        wynik=a-b
        self.ostatni_wynik=wynik
        print(wynik)

calc = Calculator() #tworzymy obiekt
calc.dodaj(5,6)

calc2=Calculator()
calc2.dodaj(10,10)

print(calc.liczba)
print(calc2.liczba)

calc.dodaj(123,34)
print("Ostatni wynik = {}".format(calc.ostatni_wynik))


