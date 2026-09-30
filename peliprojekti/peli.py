# LISÄÄ PAHVI JA BIOJÄTE
# "Pelin voi pelata läpi ja vähintään 3 erilaista reittiä"

import random

from roska import Roska
from paikka import Paikka
from pelaaja import Pelaaja


def etsi_roska(roskat):
    i = random.randint(0, len(roskat) - 1)
    return roskat[i]


nimi = input("Anna pelaajan nimi: ")
ikä = int(input("Anna pelaajan ikä: "))

print("Pelaajan nimi:", nimi)
print()
print("Pelaajan ikä:", ikä)

if ikä < 12:
    print("Olet liian nuori pelaamaan peliä. Peli suljetaan.")
else:
    print("Tervetuloa " + nimi + "!")
    print()
    print("Tämä on kierrätyspeli nimeltään Kierrätysseikkailu.")
    print()
    print("Tavoitteesi on löytää roskia ja kierrättää ne oikeisiin astioihin.")
    print()
    print("Jos vastaat väärin, peli päättyy.")
    print("Onnea matkaan!")
    print()


    roskat = [
        Roska("lasipullo", "lasijäte"), 
        Roska("muovipussi", "muovijäte"), 
        Roska("tölkki", "metallijäte"), 
        Roska("sanomalehti", "paperijäte"), 
        Roska("rikkinäinen puhelin", "elektroniikkajäte"),
        Roska("pahvilaatikko", "pahvijäte"),
        Roska("omena", "biojäte")]

    paikat = [Paikka("keittiö"), 
              Paikka("piha"), 
              Paikka("kauppa")]

    pelaaja = Pelaaja(nimi, paikat[0])

    komento = ""

    while komento != "lopeta":
        print ("--- PÄÄVALIKKO ---")
        print("Sijaintisi:", pelaaja.sijainti.nimi)
        print("Etsi - Etsi roska ja kierrätä se")
        print("Inventaario - Näytä kierrättämäsi roskat")
        print("Pisteet - Näytä pisteesi")
        print("Liiku - Vaihda sijaintia")
        print("Lopeta - Lopettaa pelin")

        komento = input("Anna komento: ").lower()

        if komento == "etsi":
            roska = etsi_roska(roskat)
            onnistui = pelaaja.kierrätä(roska)
            if not onnistui:
                komento = "lopeta"
        elif komento == "inventaario":
            pelaaja.näytä_kierrätetyt()
        elif komento == "pisteet":
            pelaaja.näytä_pisteet()
        elif komento == "liiku":
            pelaaja.vaihda_sijaintia(paikat)
        elif komento == "lopeta":
            print("Lopetetaan peli.")
        else:
            print("Virheellinen komento.")