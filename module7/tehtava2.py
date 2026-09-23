import random

def heita_noppaa(tahkot):
    return random.randint(1, tahkot)

tahkot = int(input("Anna nopan tahkojen määrä: "))

silmaluku = heita_noppaa(tahkot)
print(silmaluku)
while silmaluku != tahkot:
    silmaluku = heita_noppaa(tahkot)
    print(silmaluku)