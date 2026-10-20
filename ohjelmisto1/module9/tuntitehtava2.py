"""Kirjoita Merirosvolaiva-luokka, jonka ominaisuuksina ovat nimi, tykkien määrä, miehistön määrä ja kulta.

Alustaja saa parametreina:
laivan nimen
tykkien määrän
miehistön määrän

Uuden laivan kultamäärä asetetaan automaattisesti nollaksi.

Lisää luokkaan metodi:
loyda_aarre(maara)

Metodi kasvattaa laivan kultamäärää parametrina saadun määrän verran.

Lisää tämän jälkeen toinen metodi:
meneta_kultaa(maara)

Metodi vähentää laivan kultamäärää. Kultamäärä ei kuitenkaan koskaan saa mennä alle nollan.

Kirjoita pääohjelma, jossa:

Luodaan laiva nimeltä "The Black Pearl", jolla on 12 tykkiä ja 40 miehistön jäsentä.
Laiva löytää 200 kultaa.
Laiva löytää vielä 75 kultaa.
Laiva menettää 100 kultaa.
Tulostetaan laivan kaikki ominaisuudet.


Lisätehtävänä voit tehdä metodin:

palkkaa_miehistöä(maara)

joka kasvattaa laivan miehistön määrää. """

class Merirosvolaiva:
    def __init__(self, nimi, tykkien_maara, miehiston_maara, kulta=0):
        self.nimi = nimi
        self.tykkien_maara = tykkien_maara
        self.miehiston_maara = miehiston_maara
        self.kulta = kulta

    def loyda_aarre(self, maara):
        self.kulta = self.kulta + maara

    def meneta_kultaa(self, maara):
        self.kulta = self.kulta - maara
        if self.kulta < 0:
            self.kulta = 0
    def palkkaa_miehistoa(self, maara):
        self.miehiston_maara = self.miehiston_maara + maara


# Pääohjelma (main program)
laiva1 = Merirosvolaiva("The Black Pearl", 12, 40)

laiva1.loyda_aarre(200)
laiva1.loyda_aarre(75)
laiva1.meneta_kultaa(100)

print(f"Nimi: {laiva1.nimi}")
print(f"Tykkien määrä: {laiva1.tykkien_maara}")
print(f"Miehistön määrä: {laiva1.miehiston_maara}")
print(f"Kulta: {laiva1.kulta}")