#slownik
slownik={"wiek":"5", "imie":"Ania"}

#print(type(slownik))
print(slownik["imie"] + " ma: " + slownik["wiek"] + " lat.")
print(slownik.keys())

#krotki / tuple

lista_tupla=("fajka", "jajka")

x=lista_tupla.count("fajka")

#print(x)

#lista
produkty = ["jajko", "banan", "karmel","karmel"]
nabial = ["mleko", "ser", "twarog"]

#x=input("Co chcesz dodac do listy? ")
produkty.append(x)

x=produkty.count("karmel")

produkty.insert(3, "pomidor")

produkty.extend(nabial)

print(produkty[-1])
print(produkty)
print(type(produkty))
print(x)


