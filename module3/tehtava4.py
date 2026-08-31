# Kirjoita ohjelma, joka kysyy kolme kokonaislukua. 
# Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

luku1_str = input("Anna ensimmäinen kokonaisluku: ")
luku2_str = input("Anna toinen kokonaisluku: ")
luku3_str = input("Anna kolmas kokonaisluku: ")

luku1 = int(luku1_str)
luku2 = int(luku2_str)
luku3 = int(luku3_str)

summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = summa / 3

print(f"Lukujen summa on: {summa}")
print(f"Lukujen tulo on: {tulo}")
print(f"Lukujen keskiarvo on: {keskiarvo}")