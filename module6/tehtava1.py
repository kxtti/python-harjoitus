import random

lukumaara = int(input("Anna arpakuutioiden lukumäärä: "))

summa = 0
for i in range(lukumaara):
    silmaluku = random.randint(1, 6)
    summa = summa + silmaluku

print("Silmälukujen summa on:", summa)