import random

def heita_noppaa():
    return random.randint(1, 6)

silmaluku = heita_noppaa()
print(silmaluku)
while silmaluku != 6:
    silmaluku = heita_noppaa()
    print(silmaluku)