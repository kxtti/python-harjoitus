import random

from roska import Roska
from paikka import Paikka
from pelaaja import Pelaaja


# Valitsee roskalistasta satunnaisen roskan
def etsi_roska(roskat):
    i = random.randint(0, len(roskat) - 1)
    return roskat[i]


# Pelaaja valitsee yhden kolmesta reitistä
def valitse_reitti():
    while True:
        print()
        print("--- VALITSE REITTI ---")
        print()

        print("1 - Kotireitti")
        print("Helppo - Kierrätä 5 roskaa oikein")
        print("Keittiö, Kylpyhuone ja Autotalli")
        print()

        print("2 - Kaupunkireitti")
        print("Keskitaso - Kierrätä 10 roskaa oikein")
        print("Kauppa, Koulu ja Bussipysäkki")
        print()

        print("3 - Luontoreitti")
        print("Vaikea - Kierrätä 15 roskaa oikein")
        print("Metsä, Ranta ja Retkeilyalue")
        print()

        valinta = input("Valitse reitti (1/2/3): ")

        if valinta == "1":
            return "Kotireitti"

        elif valinta == "2":
            return "Kaupunkireitti"

        elif valinta == "3":
            return "Luontoreitti"

        else:
            print()
            print("Virheellinen valinta. Valitse 1, 2 tai 3.")


# Tallentaa pelaajan pelitilanteen tekstitiedostoon
def tallenna_peli(pelaaja, reitti):
    with open("tallennus.txt", "w", encoding="utf-8") as tiedosto:
        tiedosto.write(pelaaja.nimi + "\n")
        tiedosto.write(reitti + "\n")
        tiedosto.write(pelaaja.sijainti.nimi + "\n")

        for roska in pelaaja.kierrätetyt:
            tiedosto.write(roska + "\n")

    print()
    print("Peli tallennettu!")
    print()


# Lataa pelaajan pelitilanteen tekstitiedostosta
def lataa_peli(pelaaja, paikat, reitti):
    try:
        with open("tallennus.txt", "r", encoding="utf-8") as tiedosto:
            rivit = tiedosto.readlines()

    except FileNotFoundError:
        print()
        print("Tallennusta ei löydy.")
        print()
        return False

    # Tallennuksessa pitää olla vähintään nimi, reitti ja sijainti
    if len(rivit) < 3:
        print()
        print("Tallennustiedosto ei sisällä tarpeeksi tietoa.")
        print()
        return False

    tallennettu_nimi = rivit[0].strip()
    tallennettu_reitti = rivit[1].strip()

    # Tallennus ladataan vain, jos pelaajan nimi täsmää
    if tallennettu_nimi.lower() != pelaaja.nimi.lower():
        print()
        print("Tälle pelaajalle ei löytynyt tallennusta!")
        print()
        return False

    # Tallennus ladataan vain oikealla reitillä
    if tallennettu_reitti != reitti:
        print()
        print("Tallennuksesi on reitillä:", tallennettu_reitti)
        print("Valitse sama reitti ladataksesi tallennuksen.")
        print()
        return False

    tallennettu_sijainti = rivit[2].strip()

    # Etsitään tallennettu sijainti paikkalistasta
    for paikka in paikat:
        if paikka.nimi == tallennettu_sijainti:
            pelaaja.sijainti = paikka

    # Tyhjennetään nykyinen lista ennen tallennuksen lataamista
    pelaaja.kierrätetyt = []

    # Kolme ensimmäistä riviä ovat nimi, reitti ja sijainti
    rivin_numero = 0

    for roska in rivit:
        if rivin_numero >= 3:
            pelaaja.kierrätetyt.append(roska.strip())

        rivin_numero = rivin_numero + 1

    print()
    print("Tallennettu peli ladattu!")
    print()
    print("Reitti:", reitti)
    print()
    print("Sijaintisi:", pelaaja.sijainti.nimi)
    print()
    print("Pisteesi:", len(pelaaja.kierrätetyt))
    print()

    return True


# Kysytään pelaajan tiedot
nimi = input("Anna pelaajan nimi: ")

while True:
    try:
        ikä = int(input("Anna pelaajan ikä: "))
        break

    except ValueError:
        print()
        print("Tuo ei ole ikä perkele! Laita numeroina.")


print()
print("Pelaajan nimi:", nimi)
print()
print("Pelaajan ikä:", ikä)
print()


if ikä < 12:
    print("Olet liian nuori pelaamaan peliä. Peli suljetaan.")

else:
    print("Tervetuloa " + nimi + "!")
    print()

    # Luetaan pelin esittelyteksti intro.txt filusta
    try:
        with open("intro.txt", "r", encoding="utf-8") as tiedosto:
            intro = tiedosto.read()

        print(intro)
        print()

    except FileNotFoundError:
        print("intro.txt-tiedostoa ei löydy.")
        print()


    # Luetaan pelin ohjeet ohjeet.txt filusta
    try:
        with open("ohjeet.txt", "r", encoding="utf-8") as tiedosto:
            ohjeet = tiedosto.read()

        print(ohjeet)
        print()

    except FileNotFoundError:
        print("ohjeet.txt-tiedostoa ei löydy.")
        print()


    # Pelaaja valitsee reitin
    reitti = valitse_reitti()


    # Kaupunkireitti
    if reitti == "Kaupunkireitti":

        tavoite = 10

        paikat = [
            Paikka("Kauppa"),
            Paikka("Koulu"),
            Paikka("Bussipysäkki")
        ]

        # Kaupan roskat
        paikka1_roskat = [
            Roska("Tölkki", "metallijäte"),
            Roska("Muovipussi", "muovijäte"),
            Roska("Pahvilaatikko", "pahvijäte"),
            Roska("Lasipullo", "lasijäte")
        ]

        # Koulun roskat
        paikka2_roskat = [
            Roska("Sanomalehti", "paperijäte"),
            Roska("Kirjekuori", "paperijäte"),
            Roska("Latauskaapeli", "elektroniikkajäte"),
            Roska("Karkkipaperi", "muovijäte")
        ]

        # Bussipysäkin roskat
        paikka3_roskat = [
            Roska("Tölkki", "metallijäte"),
            Roska("Karkkipaperi", "muovijäte"),
            Roska("Muovikassi", "muovijäte"),
            Roska("Lasipullo", "lasijäte")
        ]


    # Luontoreitti
    elif reitti == "Luontoreitti":

        tavoite = 15

        paikat = [
            Paikka("Metsä"),
            Paikka("Ranta"),
            Paikka("Retkeilyalue")
        ]

        # Metsän roskat
        paikka1_roskat = [
            Roska("Muovikassi", "muovijäte"),
            Roska("Karkkipaperi", "muovijäte"),
            Roska("Ruosteinen naula", "metallijäte"),
            Roska("Lasipullo", "lasijäte")
        ]

        # Rannan roskat
        paikka2_roskat = [
            Roska("Viinipullo", "lasijäte"),
            Roska("Tölkki", "metallijäte"),
            Roska("Muovipussi", "muovijäte"),
            Roska("Karkkipaperi", "muovijäte")
        ]

        # Retkeilyalueen roskat
        paikka3_roskat = [
            Roska("Omena", "biojäte"),
            Roska("Päärynä", "biojäte"),
            Roska("Banaaninkuori", "biojäte"),
            Roska("Tölkki", "metallijäte")
        ]


    # Kotireitti
    else:

        tavoite = 5

        paikat = [
            Paikka("Keittiö"),
            Paikka("Kylpyhuone"),
            Paikka("Autotalli")
        ]

        # Keittiön roskat
        paikka1_roskat = [
            Roska("Banaaninkuori", "biojäte"),
            Roska("Omena", "biojäte"),
            Roska("Hillopurkki", "lasijäte"),
            Roska("Pizzalaatikko", "pahvijäte")
        ]

        # Kylpyhuoneen roskat
        paikka2_roskat = [
            Roska("Shampoopullo", "muovijäte"),
            Roska("Muovipussi", "muovijäte"),
            Roska("Paristo", "elektroniikkajäte"),
            Roska("Hillopurkki", "lasijäte")
        ]

        # Autotallin roskat
        paikka3_roskat = [
            Roska("Kattila", "metallijäte"),
            Roska("Ruosteinen naula", "metallijäte"),
            Roska("Latauskaapeli", "elektroniikkajäte"),
            Roska("Pahvilaatikko", "pahvijäte")
        ]


    print()
    print("Valitsit:", reitti)
    print("Tavoite:", tavoite, "roskaa")
    print()


    # Luodaan pelaaja ja aloitussijainniksi reitin ensimmäinen paikka
    pelaaja = Pelaaja(nimi, paikat[0])


    # Pelaaja voi jatkaa aikaisemmin tallennettua peliä
    jatka = input(
        "Haluatko jatkaa aikaisemmin tallennettua peliä? (kyllä/ei): "
    ).lower()

    if jatka == "kyllä":
        lataa_peli(pelaaja, paikat, reitti)


    komento = ""


    # Pelin pääsilmukka
    while komento != "lopeta":
        print()
        print("--- PÄÄVALIKKO ---")
        print()
        print("Reitti:", reitti)
        print("Sijaintisi:", pelaaja.sijainti.nimi)
        print("Pisteesi:", len(pelaaja.kierrätetyt), "/", tavoite)
        print()
        print("Etsi - Etsi roska ja kierrätä se")
        print("Inventaario - Näytä kierrättämäsi roskat")
        print("Pisteet - Näytä pisteesi")
        print("Liiku - Vaihda sijaintia")
        print("Tallenna - Tallenna pelin tilanne")
        print("Lopeta - Lopettaa pelin")
        print()

        komento = input("Anna komento: ").lower()


        if komento == "etsi":

            # Valitaan roskat nykyisen sijainnin perusteella
            if pelaaja.sijainti.nimi == paikat[0].nimi:
                roska = etsi_roska(paikka1_roskat)

            elif pelaaja.sijainti.nimi == paikat[1].nimi:
                roska = etsi_roska(paikka2_roskat)

            else:
                roska = etsi_roska(paikka3_roskat)


            onnistui = pelaaja.kierrätä(roska)


            # Väärä vastaus lopettaa pelin
            if not onnistui:
                komento = "lopeta"


            # Reitin tavoitteen saavuttaminen läpäisee pelin
            elif len(pelaaja.kierrätetyt) >= tavoite:
                print()
                print("================================")
                print()
                print("ONNEKSI OLKOON!")
                print()
                print("Kierrätit", tavoite, "roskaa oikein.")
                print("Läpäisit valitsemasi reitin!")
                print("Voitit Kierrätysseikkailun!")
                print()
                print("================================")
                print()

                komento = "lopeta"


        elif komento == "inventaario":
            pelaaja.näytä_kierrätetyt()


        elif komento == "pisteet":
            pelaaja.näytä_pisteet()


        elif komento == "liiku":
            pelaaja.vaihda_sijaintia(paikat)


        elif komento == "tallenna":
            tallenna_peli(pelaaja, reitti)


        elif komento == "lopeta":
            print()
            print("Lopetetaan peli.")
            print()


        else:
            print()
            print("Virheellinen komento.")
            print()