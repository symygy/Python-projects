import sqlite3
import os

def pobierz_dane(plikcsv):
    #deklarujemy pusta liste
    dane = []
    if os.path.isfile(plikcsv): #sprawdzamy czy plik istnieje na dysku
        # otwieramy plik do odczytu
        with open(plikcsv, "r") as zawartosc:
            for linia in zawartosc:
                linia = linia.replace("\n", "") #usuwamy znaki konca lini
                linia = linia.replace("\r", "") #usuwamy znaki konca lini
                #linia = linia.decode("utf-8") #odczytujemy znaki jako utf
                # dodajemy elementy do tupli a tuple do listy
                dane.append(tuple(linia.split(",")))
    else:
        print("Plik nie iestnieje")

    return tuple(dane) # przeksztalcamy liste na tuple i zwracamy ja

#tworzymy polaczenie z baza przechowywana na dysku lub w pamieci (':memory:')
con = sqlite3.connect('test.db')

#dostep do kolumn przez indeksy i przez nazwy
con.row_factory = sqlite3.Row #umozliwa dostep do kolumn nie tylko przez indeksy ale rowniec przez nazwy

#utworzenie obiektu kursora
cur = con.cursor()

# Zanim będziemy mogli wykonywać podstawowe operacje na bazie danych określane skrótem CRUD – Create (tworzenie),
# Read (odczyt), Update (aktualizacja), Delete (usuwanie) -
# musimy utworzyć tabele i relacje między nimi według zaprojektowanego schematu.

#tworzenie tabel
cur.execute("DROP TABLE IF EXISTS klasa;") #wykonujemy pojedyncze polecenia za pomoca metody execute obiektu kursora

cur.execute("""
CREATE TABLE IF NOT EXISTS klasa (
    id INTEGER PRIMARY KEY ASC,
    nazwa varchar(250) NOT NULL,
    profil varchar(250) DEFAULT ''
)""")

#wiele instrukcji wykonujemy za pomoca executescript
cur.executescript("""
    DROP TABLE IF EXISTS uczen;
    CREATE TABLE IF NOT EXISTS uczen (
        id INTEGER PRIMARY KEY ASC,
        imie varchar(250) NOT NULL,
        nazwisko varchar(250) NOT NULL,
        klasa_id INTEGER NOT NULL,
        FOREIGN KEY(klasa_id) REFERENCES klasa(id)
    )""")

# wstawiamy jeden rekord danych
cur.execute('INSERT INTO klasa VALUES(NULL, ?, ?);',('1A', 'matematyczny'))
cur.execute('INSERT INTO klasa VALUES(NULL, ?, ?);', ('1B', 'humanistyczny'))

# wykonujemy zapytanie SQL, ktore pobierze z id klasy 1A z tabeli klasa
# Jeżeli podajemy jedną wartość w tupli jako argument metody .execute(), musimy pamiętać o umieszczeniu
# dodatkowgo przecinka, np. ('1A',), ponieważ w ten sposób tworzymy w Pythonie 1-elementowe tuple.
# W przypadku wielu wartości przecinek nie jest wymagany.
cur.execute('SELECT id FROM klasa WHERE nazwa = ?', ('1A',))

#Metoda .fechone() kursora zwraca listę zawierającą pola wybranego rekordu.
# Jeżeli interesuje nas pierwszy, i w tym wypadku jedyny, element tej listy dopisujemy [0]
klasa_id = cur.fetchone()[0]

#tupla uczniowie zawiera tuple z danymi poszczegolnych oczniow

uczniowie = (
    (None, 'Tomasz', 'Nowak', klasa_id),
    (None, 'Jan', 'Kos', klasa_id),
    (None, 'Piotr', 'Kowalski', klasa_id)
)

uczniowie = pobierz_dane('uczniowie.csv')

# nie warto umieszczac wartosci pol bezposrednio w zapytaniu SQL ze wzgledu na mozliwe bledy lub ataki typu
# SQL injection. Zamiast tego uzywamy zastepnikow w postaci znakow zapytania. Wartosci przekazujemy w tupli jako
# drugi argument

##wstawiamy wiele rekordow
cur.executemany('INSERT INTO uczen VALUES(?, ?, ?, ?)', uczniowie)

#zatwierdzamy zmiany w bazie
con.commit()

# pobieranie danych z bazy
def czytajdane():
    """funkcja pobiera i wyswietla dane z bazy"""
    cur.execute(
        """
        SELECT uczen.id, imie, nazwisko, nazwa FROM uczen, klasa
        WHERE uczen.klasa_id=klasa.id
        """)
    uczniowie = cur.fetchall()
    for uczen in uczniowie:
        print(uczen['id'], uczen['imie'], uczen['nazwisko'], uczen['nazwa'])
        print()



#Funkcja czytajdane() wykonuje zapytanie SQL pobierające wszystkie dane z dwóch powiązanych tabel: “uczen” i “klasa”.
# Wydobywamy id ucznia, imię i nazwisko, a także nazwę klasy na podstawie warunku w klauzuli WHERE.
# Wynik, czyli wszystkie pasujące rekordy zwrócone przez metodę .fetchall(), zapisujemy w zmiennej
# uczniowie w postaci tupli. Jej elementy odczytujemy w pętli for jako listę uczen.
# Dzięki ustawieniu właściwości .row_factory połączenia z bazą na sqlite3.Row odczytujemy poszczególne pola
# podając nazwy zamiast indeksów, np. uczen['imie'].
czytajdane()

# zmiana klasy ucznia o identyfikatorze 2
cur.execute('SELECT id FROM klasa WHERE nazwa = ?', ('1B',))
klasa_id = cur.fetchone()[0]
cur.execute('UPDATE uczen SET klasa_id=? WHERE id=?', (klasa_id, 2))

# usunięcie ucznia o identyfikatorze 3
cur.execute('DELETE FROM uczen WHERE id=?', (3,))

czytajdane()


