

fruits = ['apple', 'orange', 'pear', 'banana', 'apple']
print("rozpoczynam petle {} {}".format("siemanko","elo")) #doda siema w nawiasie {} a potem elo w nastepnym
for i, fruit in enumerate(fruits):
    print("Sprawdzam nr: {}".format(i))
    if i==3:
        break

    print(i)
    print(fruit)

print("Koniec")

x="Hello {}"
y=x.format("world")

print(x)
print(y)

