luvut = []

syote = input("Anna luku tai lopeta painamalla Enter: ")
while syote != "":
    luku = int(syote)
    luvut.append(luku)
    syote = input("Anna seuraava luku tai lopeta painamalla Enter: ")

luvut.sort(reverse=True)

print("Viisi suurinta lukua:")
for i in range(5):
    print(luvut[i])