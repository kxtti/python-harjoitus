"""Kirjoita Pelaaja-luokka, jonka ominaisuuksia ovat nimi, elämät, kolikot ja pisteet. 
Kirjoita luokkaan alustaja, joka saa parametrina hahmon nimen. Uuden hahmon elämät asetetaan automaattisesti 
arvoon 3. Kolikot asetetaan arvoon 0. Pisteet asetetaan arvoon 0.

Kirjoita pääohjelma, jossa luot Pelaaja-olion nimeltä "Mario". Tulosta tämän jälkeen kaikki hahmon ominaisuudet."""


class Pelaaja:
    def __init__(self, nimi, elämät=3, kolikot=0, pisteet=0):
        self.nimi = nimi
        self.elämät = elämät
        self.kolikot = kolikot
        self.pisteet = pisteet

# Pääohjelma (main program)
pelaaja1 = Pelaaja("Maaaario")

print(f"{pelaaja1.nimi}\nElämät: {pelaaja1.elämät}")
print(f"Kolikot: {pelaaja1.kolikot}")
print(f"Pisteet: {pelaaja1.pisteet}")

