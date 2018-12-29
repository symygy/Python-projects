import time


class PhoneBook():

    #def __init__(self):


    def __del__(self):
        self.file.close()

    def f_open(self):
        self.file = open("PhoneBook.txt", mode='a+')

    def f_save(self, tekst):
        self.file.write(tekst)
        print("\n Pomyślnie dodano czlowieka \n")
        time.sleep(2)

    def show_people(self):
        self.file = open("PhoneBook.txt", mode='r')
        for line in self.file.readlines():
            print(line.rstrip())

    def cout_people(self):
        self.ilosc=0
        self.file = open("PhoneBook.txt", mode='r')
        for line in self.file.readlines():
            self.ilosc += 1
        return self.ilosc

    def erease_data(self):
        self.file = open("PhoneBook.txt", mode='w+')
        self.file.close()

    def delete(self, id):
        self.file = open("PhoneBook.txt", mode='r+')
        self.file.seek(0)
        for line in self.file.readlines():
            if line != id:
                self.file.write(line + '\n')
        self.file.truncate()
        self.file.close()

wybor = 0

while True:
    klient1 = PhoneBook()
    ilosc_ludzi = klient1.cout_people()

    print("""
    *******  Aktualna ilosc ludzi w bazie: {}   *******""".format(klient1.cout_people()))

    wybor = input("""
    1. Dodaj czlowieka
    2. Usun czlowieka
    3. Wypisz ludzi
    4. Wyczysc plik
    5. Zakoncz program
    """)


    if wybor == '1':
        klient1.f_open()
        klient1.id = ilosc_ludzi+1
        klient1.imie = input("Podaj imie: ")
        klient1.nazwisko = input("Podaj nazwisko: ")
        klient1.telefon = input("Podaj telefon: ")
        klient1.dane = "id" + str(klient1.id) + " " + klient1.imie + " " + klient1.nazwisko + " " + klient1.telefon + "\n"
        klient1.f_save(klient1.dane)

    if wybor == '2': # nie dziala
        usun=input("Podaj id klienta ktorego chcesz usunac: ")
        klient1.delete(usun)

    if wybor == '3':
        if klient1.cout_people() > 0:
            print("Format wyświetlania:")
            print("ID | Imie | Nazwisko | Numer telefonu \n")
            klient1.show_people()
        else:
            print("""
            Baza danych jest pusta! """)

    if wybor == '4':
        print("Czy na pewno chcesz wyczyscic plik? ")
        decyzja = input("Wpisz y lub n: ")
        if decyzja == 'y':
            klient1.erease_data()
            time.sleep(1)
            print("Usunieto plik danych.")
            continue
        elif decyzja == 'n':
            print("Anulowanie usuniecie pliku.")
            time.sleep(1)
            continue
        else:
            print("Wybrano zla litere")
            time.sleep(1)
            continue

    if wybor == '5':
        exit()

    #else:
        #print("Nie ma takiego numeru! ")