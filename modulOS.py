import os

#listowanie plikow i katalogow
lista=os.listdir(".")  #jak wpisze "." to wylistuje pliki z aktualnego folderu w ktorym odpalam pliki
print(lista)

for element in lista:
    if os.path.isfile(element): # jesli element jest plikiem to zwraca wartosc True
        print("{} jest plikiem".format(element))
    if os.path.isdir(element): #sprawdza czy element jest folderem
        print("{} jest folderem".format(element))

# oprocz plikow i folderow istnieja jeszcze "nawiazania" wiec lepiej sprawdzac osobno czy jest to plik cyz folder zamiast else

# os.mkdir("pliki") - tworzy folder
# os.rename("test.txt", "plik.txt") #zmienia nazwe pliki z plik na test
# os.remove("plik.txt") - usuwa plik
# os.rmdir(pliki - usuwa folder

path="Testowy/01/dane.txt"
#os.makedirs(path) #utworz foldery
print(os.path.dirname(path)) #zwraca to co jest przed ostatnim slashem w sciezce
print(os.path.basename(path)) #zwraca to co jest po ostatnim slashu w sciezce
print(os.path.abspath(path)) #zwraca kompletna sciezke

dir_path = os.path.dirname(path)
os.makedirs(dir_path)
open(path,mode='w').close()







