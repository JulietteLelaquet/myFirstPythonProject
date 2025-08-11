from random import*

liste=[]
nb=int(input("Saisissez le nombre d'entier dans la liste :"))

for i in range (0,nb):
    liste.append(randint(0, 1000))
    i += 1

print("La liste avant le tri est : ", liste)
liste.sort()
print("La liste après le tri est : ", liste)

nb1=int(input("Saisissez le nombre que vous souhaitez ajouter à la liste :"))

a=0
while a<nb and liste[a]<nb1:
    a+=1
liste.insert(a, nb1)
print("La liste apres insertion est : ", liste)
