try:
    plik = open("jajeczko.txt", mode='r+')
    plik.write("Hello")
    plik.close()
except FileNotFoundError:
    print("Nie ma pliku takiego")

try:
    plik2 = open("jajeczko2.txt", mode='r')
    plik2.write("Hello")
    plik2.close()
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print("Nieznany blad")
    print(e)

