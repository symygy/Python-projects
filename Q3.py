x=input("Podaj liczbe: ")
x=int(x)
slownik = {}

for i in range(0, x):
    z = str(i)
    slownik[z]=i*i

print(slownik)