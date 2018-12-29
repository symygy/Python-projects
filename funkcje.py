def funkcja(x):
    print(x)
z="siemanko"
funkcja(z)



def mnoz(a,b=2):  #domyslnie wezmie 2 jesli nie ma drugiego argumentu
    a=int(a)
    b=int(b)
    return a*b

a = input("podaj liczbe a: ")
b = input("podaj liczbe b: ")

wynik = mnoz(a,b)
print(wynik)

