x = input("Podaj liczbe: ")
x=int(x)

def silnia(x):
    if x<=1: return 1
    else: return x*silnia(x-1)


print(silnia(x))