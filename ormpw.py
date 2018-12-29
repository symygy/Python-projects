import os
from time import sleep
from peewee import *

#if os.path.exists('test.db'):
    #os.remove('test.db')
# tworzymy instancje bazy uzywanej przez modele
baza = SqliteDatabase('test.db')  # ':memory:'

class BazaModel(Model):
    class Meta:
        database = baza

# klasy klasa i uczen opisuja rekordy tabel: klasa i uczen oraz relacje miedzy nimi

class Klasa(BazaModel):
    nazwa = CharField(null=False)  # null=False nie zezwala na pozostawienie wartosci pustej
    profil = CharField(default='')  # default czyli wartosc domyslne


class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')


baza.connect()  # nawiazujemy polaczenie z baza
baza.create_tables([Klasa, Uczen])  # tworzymy baze

# dodajemy dwie klasy jesli tabela jest pusta
if Klasa().select().count() == 0:
    inst_klasa = Klasa(nazwa='1A', profil='matematyczny')
    inst_klasa.save()
    inst_klasa = Klasa(nazwa='1B', profil='humanistyczny')
    inst_klasa.save()

# tworzymy instancje klasy Klasa reprezentujaca klase "1A"
inst_klasa = Klasa.select().where(Klasa.nazwa == '1A').get()
inst_klasa2 = Klasa.select().where(Klasa.nazwa == '1B').get()

# lista ucznikow ktorych dane zapisane sa w slownikach
uczniowie = []
    # dodajemy dane wielu uczniow
#Uczen.insert_many(lista).execute()
#Uczen.insert_many(uczniowie2).execute()


# odczytujemy dane z bazy

def czytajDane():
    print("id | imie | nazwisko | klasa")
    for uczen in Uczen.select().join(Klasa):
        print(uczen.id, uczen.imie, uczen.nazwisko, uczen.klasa.nazwa)


print("--------------------------------")

while True:
    print("""MENU:
    1. Wyswietl uczniow w bazie 
    2. Dodaj
    3. Usun
    4. Modyfikuj
    5. Koniec""")

    wybor = input("Podaj numer: ")

    if wybor =='1':
        czytajDane()

    elif wybor == '2':
        imieDodaj = input("Podaj imie: ")
        nazwiskoDodaj = input("Podaj nazwisko: ")
        klasaDodaj = input("Wybierz klase - 1A lub 1B: ")

        if klasaDodaj == "1A":
            dodawanie = {'imie': imieDodaj, 'nazwisko': nazwiskoDodaj, 'klasa': inst_klasa}
            Uczen.insert(dodawanie).execute()
        elif klasaDodaj == "1B":
            dodawanie = {'imie': imieDodaj, 'nazwisko': nazwiskoDodaj, 'klasa': inst_klasa2}
            Uczen.insert(dodawanie).execute()

    elif wybor == '3':
        czytajDane()
        uczenID = input("Podaj numer id ucznia ktorego chcesz usunac: ")
        try:
            print("Czy potwierdzasz, ze chcesz usunac ucznia o danych: ")
            inst_uczen = Uczen().select().join(Klasa).where(Uczen.id == uczenID).get()
            print(inst_uczen.id, inst_uczen.imie, inst_uczen.nazwisko, inst_uczen.klasa.nazwa)

        except:
            print ("Nie ma ucznia o takim ID.")
            print ("Powrot do glownego menu.")
            sleep(2)
            continue

        usunYesNo = input("Wpisz y lub n: ")

        if usunYesNo == 'y':
            inst_uczen.get().delete_instance()
            print ("Usunieto ucznia o id: {}".format(uczenID))
            sleep(2)
            continue
        elif usunYesNo == 'n':
            print("Anulowano usuniecie ucznia.")
            sleep(2)
            continue

    elif wybor == '4':
        czytajDane()
        uczenID = input("Podaj numer id ucznia ktorego chcesz zmodyfikowac: ")
        try:
            inst_uczen = Uczen().select().join(Klasa).where(Uczen.id == uczenID).get()
        except:
            print("Nie ma ucznia o takim ID.")
            print("Powrot do glownego menu.")
            sleep(2)
            continue
        inst_uczen = Uczen().select().join(Klasa).where(Uczen.id == uczenID).get()
        imieDodaj = input("Podaj imie: ")
        nazwiskoDodaj = input("Podaj nazwisko: ")
        klasaDodaj = input("Wybierz klase - 1A lub 1B: ")
        inst_uczen.imie = imieDodaj
        inst_uczen.nazwisko = nazwiskoDodaj
        if klasaDodaj == '1A':
            inst_uczen.klasa = inst_klasa
        elif klasaDodaj == '1B':
            inst_uczen.klasa = inst_klasa2

        inst_uczen.save()

    elif wybor == '5':
        baza.close()
        exit()


# zmiana klasy ucznia o identyfikatorze 2
#inst_uczen = Uczen().select().join(Klasa).where(Uczen.id == 2).get()
#inst_uczen.klasa = Klasa.select().where(Klasa.nazwa == '1B').get()
#inst_uczen.save()  # zapisanie zmian w bazie

# usunięcie ucznia o identyfikatorze 3
#Uczen.select().where(Uczen.id == 3).get().delete_instance()

czytajDane()

