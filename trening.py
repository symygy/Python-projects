def dodawanie(x,y):
    wynik=float(x+y)
    return wynik

def odejmowanie(x,y):
    wynik = float(x - y)
    return wynik

def dzielenie(x,y):
    wynik = float(x / y)
    return wynik

lista=[]
#y=input("Ile osob ma liczyc lista?")

#for i in range(0,int(y)):

#    x=input("Podaj imie: ")
#    lista.append(x)
#    print(lista)

#if len(lista) > 5:
#    z=" imion"
#else:
#    z = " imiona"

#print("Lista zawiera: " + str(len(lista)) + z)

a=input("podaj a: ")
a=int(a)
b=input("Podaj b: ")
b=int(b)

while True:
    z=input("""1. Dodawnie
    2. Odejmowanie
    3. Dzielenie
    Wybierz odpowiednia cyfre: """)

    z=int(z)

    if z == 1:
        print(str(dodawanie(a,b)))

    elif z==2:
        print(str(odejmowanie(a,b)))

    elif z==3:
        print(str(dzielenie(a,b)))

    else:
        print("Nie ma takiej cyfry luju.")

