
file = open("plik2.txt", mode = 'a+')  # r- tylko odczyt, w-odczyt i zapisa, w+-odczyt/zapis/utworzenie pliku, ale przy utworzeniu usuwa zawartosc,
# a+ to samo co w+ tylko nie usuwa zawartosci pliku
file.write("123\n")
file.close() # trzeba zamknac otwarty  plik

file2=open("plik2.txt", mode='r')
#print(file2.readlines()) wypisuje wszystko z pliku, jak plik jest duzy to malo efektywne

for line in file2.readlines():
    #print(line, end="")
    print(line.rstrip()) #usuwa biale znaki z prawej strony stringa
    #strip - usuwa biale znaki z lewej i z prawej strony stringa
file2.close()


