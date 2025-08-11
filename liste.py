from random import*

liste = []
nb=int(input("Saisissez le nombre d'entier dans la liste :"))

for i in range (0,nb):
    liste.append(randint(0, 1000))
    i += 1

print(liste)

for i in liste:
    if i%2 ==0:
        print(i)