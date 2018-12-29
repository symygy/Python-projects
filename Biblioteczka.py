import sqlite3

class Czytelnik:
    def __init__(self, im="Jan", nazw="Nowak", numer_karty="123"):
        self.imie = im
        self.nazwisko = nazw
        self.nr_karty = numer_karty

class Ksiazka:
    def __init__(self, autor="", tytul="", isbn="", liczba_egz=0, liczba_wyp=0, ):
        self.autor = autor
        self.tytul = tytul
        self.isbn = isbn
        self.liczba_egz = liczba_egz
        self.liczba_wyp = liczba_wyp

class Wypozyczone:
    def __init__(self, ksiazka="", czytelnik=""):
        self.ksiazka = ksiazka
        self.czytelnik = czytelnik

class Biblioteka:
    def __init__(self, ksiazki=[], czytelnicy=[], wypozyczenia=[]):
        self.ksiazki = ksiazki
        self.czytelnicy = czytelnicy
        self.wypozyczenia = wypozyczenia

def open_db(self):
    #stworzenie bazy
    self.connection=sqlite3.connect('file:Biblioteka.db?mode=rw', uri=True)
    # dzieki temu odczytujemy poszczegolne pola podajac ich nazwy zamiast indeksow
    self.connection.row_factory=sqlite3.Row

    #stworzenie kursora
    self.cur=self.connection.cursor()

def create_tables(self):
#stworzenie tabel
    self.cur.execute("DROP TABLE IF EXISTS czytelnik;")
    self.cur.execute("""
    CREATE TABLE IF NOT EXISTS czytelnik (
        nrKarty INTEGER PRIMARY KEY ASC,
        imie VARCHAR(250) NOT NULL,
        nazwisko VARCHAR(250) NOT NULL )
    """)

    self.cur.executescript("""
    DROP TABLE IF EXISTS ksiazka; 
    CREATE TABLE IF NOT EXISTS ksiazka (
        isbn integer primary key asc,
        autor varchar(250) not null,
        tytul varchar(250) not null,
        liczba_egz integer,
        liczba_wyp integer,
        czytelnikId integer not null,
        foreign key(czytelnikId) references czytelnik(nrKarty) 
    )""")

    self.cur.executescript("""
    DROP TABLE IF EXISTS wypozyczone; 
    CREATE TABLE IF NOT EXISTS wypozyczone (
        id integer primary key asc,
        ksiazkaISBN integer not null,
        czytelnikId integer not null,
        foreign key(ksiazkaISBN) references ksiazka(isbn),
        foreign key(czytelnikId) references czytelnik(nrKarty)
    )""")
def close_db(self):
    # zamykamy baze
        self.connection.close()


def main():

    B1 = Biblioteka()
    C1 = Czytelnik()
    K1 = Ksiazka()
    W1 = Wypozyczone()

    while(True):
        print("Menu:")
        print("""
        1. Dodaj czytelnika
        2. Usun czytelnika
        3. Dodaj ksiazke
        4. Usun ksiazke
        5. Wypozycz ksiazke
        6. Oddaj ksiazke
        7. Lista czytelnikow
        8. Koniec
        """)

        wybor=input()

        if wybor == '1':
            C1.im = input("Podaj imie: ")
            C1.nazw = input("Podaj nazwisko: ")
            cur.execute('insert into czytelnik values(NULL, ?, ?);', (C1.im, C1.nazw))
            connection.commit() # zamykamy baze i zapisujemy zmiany
            # bez przecinka python widzi C1.nazw jako ciag znakow
            cur.execute('select nrKarty from czytelnik where nazwisko=(?);', (C1.nazw,))
            C1.nr_karty = cur.fetchall()
            print("Dodano nowego czytelnika: ")
            print("Imie: " + C1.im)
            print("Nazwisko: " + C1.nazw)

            # wszystkie pasujace rekordy zwrocone w fetchall zapisujemy do zmiennej czytelnik jako tupla
            for czytelnik in C1.nr_karty:
                print("Numer karty: " + str(czytelnik['nrKarty']))
            connection.close()

        elif wybor == '2':
            open_db(self.connection)



        elif wybor == '7':
            cur.execute('select * from czytelnik')
            dane = cur.fetchall()
            for czytelnik in dane:
                print("Dane czytelnikow w bazie: ")
                print("Numer karty: "+ str(czytelnik['nrKarty']) +"  |  "+ "Nazwisko: " + str(czytelnik['nazwisko']) +"  |  "+"Imie: "+str(czytelnik['imie']))


if __name__=="__main__":
    main()
