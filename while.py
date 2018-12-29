

print("Start")

#lista=["a", "b", "b", "d", "e", "f", "g", "h", "i", "j"]
lista=[]

licznik=input("Podaj ile elementow ma liczyc lista: ")
licznik=int(licznik)
i=0
while i < licznik:
    #print(lista[i])

    numer=str(i)
    lista.append("wyraz " + numer)
    i+=1


print(lista)



