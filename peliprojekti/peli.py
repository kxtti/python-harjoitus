import random


def etsi_roska(roskat, astiat):
    i = random.randint(0, len(roskat) - 1)
    return roskat[i], astiat[i]


def kierrätä(roska, oikea_astia, kierrätetyt):
    print("Löysit:", roska)

    vastaus = input(
        "Mihin astiaan se kuuluu? "
        "(lasijäte/muovijäte/metallijäte/paperijäte/elektroniikkajäte) ").lower()

    if vastaus == oikea_astia:
        print("Oikein! Sait pisteen.")
        kierrätetyt.append(roska)
        return True
    else:
        print("Väärin! Peli päättyy.")
        return False


def näytä_kierrätetyt(kierrätetyt):
    print("Olet kierrättänyt oikein seuraavat:")

    if len(kierrätetyt) == 0:
        print("Et ole vielä kierrättänyt mitään.")
    else:
        for roska in kierrätetyt:
            print("-", roska)


def näytä_pisteet(kierrätetyt):
    print("Pisteesi:", len(kierrätetyt))


def vaihda_sijaintia(sijainti):
    print("Nykyinen sijaintisi:", sijainti)

    print("Minne haluat mennä?")
    print("Keittiö")
    print("Piha")
    print("Kauppa")

    valinta = input("Kirjoita sijainti: ").lower()

    if valinta == "keittiö":
        sijainti = "keittiö"
    elif valinta == "piha":
        sijainti = "piha"
    elif valinta == "kauppa":
        sijainti = "kauppa"
    else:
        print("Virheellinen sijainti.")

    return sijainti


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
    print("Tämä on kierrätyspeli.")
    print()
    print("Tavoitteesi on löytää roskia ja kierrättää ne oikeisiin astioihin.")
    print()
    print("Jos vastaat väärin, peli päättyy.")
    print("Onnea matkaan!")
    print()


    roskat = ["lasipullo", "muovipussi", "tölkki", "sanomalehti", "rikkinäinen puhelin"]
    astiat = ["lasijäte", "muovijäte", "metallijäte", "paperijäte", "elektroniikkajäte"]

    kierrätetyt = []

    sijainti = "keittiö"

    komento = ""

    while komento != "lopeta":

        print("--- PÄÄVALIKKO ---")
        print("Sijaintisi:", sijainti)
        print("Etsi - Etsi roska ja kierrätä se")
        print("Inventaario - Näytä kierrättämäsi roskat")
        print("Pisteet - Näytä pisteesi")
        print("Liiku - Vaihda sijaintia")
        print("Lopeta - Lopettaa pelin")
 
        komento = input("Anna komento: ").lower()
 
        if komento == "etsi":
            roska, oikea_astia = etsi_roska(roskat, astiat)
            onnistui = kierrätä(roska, oikea_astia, kierrätetyt)
            if not onnistui:
                komento = "lopeta"
        elif komento == "inventaario":
            näytä_kierrätetyt(kierrätetyt)
        elif komento == "pisteet":
            näytä_pisteet(kierrätetyt)
        elif komento == "liiku":
            sijainti = vaihda_sijaintia(sijainti)
        elif komento == "lopeta":
            print("Lopetetaan peli.")
        else: print("Virheellinen valinta.")

