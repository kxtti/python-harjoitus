import random

from roska import Roska
from paikka import Paikka
from pelaaja import Pelaaja


# Valitsee roskalistasta satunnaisen roskan
def etsi_roska(roskat):
    i = random.randint(0, len(roskat) - 1)
    return roskat[i]


# Tallentaa pelaajan pelitilanteen tekstitiedostoon
def tallenna_peli(pelaaja):
    with open("tallennus.txt", "w", encoding="utf-8") as tiedosto:
        tiedosto.write(pelaaja.nimi + "\n")
        tiedosto.write(pelaaja.sijainti.nimi + "\n")
       
        for roska in pelaaja.kierrätetyt:
            tiedosto.write(roska + "\n")

    print()
    print("Peli tallennettu!")
    print()


# Lataa pelaajan pelitilanteen tekstitiedostosta
def lataa_peli(pelaaja, paikat):
    try:
        with open("tallennus.txt", "r", encoding="utf-8") as tiedosto:
            rivit = tiedosto.readlines()

    except FileNotFoundError:
        print()
        print("Tallennusta ei löydy.")
        print()
        return False

    # Tallennuksessa pitää olla vähintään nimi ja sijainti
    if len(rivit) < 2:
        print("Tallennustiedosto ei sisällä tarpeeksi tietoa.")
        return False

    tallennettu_nimi = rivit[0].strip()

    # Tallennus ladataan vain, jos pelaajan nimi täsmää
    if tallennettu_nimi.lower() != pelaaja.nimi.lower():
        print()
        print("Tälle pelaajalle ei löytynyt tallennusta!")
        print()
        return False

    tallennettu_sijainti = rivit[1].strip()

    # Etsitään tallennettu sijainti paikkalistasta
    for paikka in paikat:
        if paikka.nimi == tallennettu_sijainti:
            pelaaja.sijainti = paikka

    # Tyhjennetään nykyinen lista ennen tallennuksen lataamista
    pelaaja.kierrätetyt = []

    # Riviltä 3 eteenpäin ovat kierrätetyt roskat
    for roska in rivit[2:]:
        pelaaja.kierrätetyt.append(roska.strip())

    print()
    print("Tallennettu peli ladattu!")
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

    # Pelissä olevat roskat ja niiden jäteastiat
    roskat = [
        Roska("Lasipullo", "lasijäte"), 
        Roska("Muovipussi", "muovijäte"), 
        Roska("Tölkki", "metallijäte"), 
        Roska("Sanomalehti", "paperijäte"), 
        Roska("Rikkinäinen puhelin", "elektroniikkajäte"),
        Roska("Pahvilaatikko", "pahvijäte"),
        Roska("Omena", "biojäte"),
        Roska("Päärynä", "biojäte"),
        Roska("Hillopurkki", "lasijäte"),
        Roska("Viinipullo", "lasijäte"),
        Roska("Shampoopullo", "muovijäte"),
        Roska("Muovikassi", "muovijäte"),
        Roska("Jäätelöpurkki", "muovijäte"),
        Roska("Kattila", "metallijäte"),
        Roska("Kirjekuori", "paperijäte"),
        Roska("Pizzalaatikko", "pahvijäte"),
        Roska("Kenkälaatikko", "pahvijäte"),
        Roska("Paristo", "elektroniikkajäte"),
        Roska("Latauskaapeli", "elektroniikkajäte"),
        Roska("Banaaninkuori", "biojäte"),
        Roska("Karkkipaperi", "muovijäte"),
        Roska("Ruosteinen naula", "metallijäte"),
        Roska("Mädäntynyt appelsiini", "biojäte")
    ]

    # Pelissä olevat sijainnit
    paikat = [
        Paikka("Keittiö"), 
        Paikka("Takapiha"), 
        Paikka("Kauppa"),
        Paikka("Metsä"),
        Paikka("Koulu")
    ]

    # Luodaan pelaaja ja sen aloitussijainniksi keittiö
    pelaaja = Pelaaja(nimi, paikat[0])

    # Pelaaja voi jatkaa aikaisemmin tallennettua peliä
    jatka = input("Haluatko jatkaa aikaisemmin tallennettua peliä? (kyllä/ei): ").lower()

    if jatka == "kyllä":
        lataa_peli(pelaaja, paikat)

    komento = ""

    # Pelin pääsilmukka, jatkuu siihen asti kunnes pelaaja kirjoittaa lopeta
    while komento != "lopeta":
        print()
        print("--- PÄÄVALIKKO ---")
        print("Sijaintisi:", pelaaja.sijainti.nimi)
        print("Etsi - Etsi roska ja kierrätä se")
        print("Inventaario - Näytä kierrättämäsi roskat")
        print("Pisteet - Näytä pisteesi")
        print("Liiku - Vaihda sijaintia")
        print("Tallenna - Tallenna pelin tilanne")
        print("Lopeta - Lopettaa pelin")
        print()

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

        elif komento == "tallenna":
            tallenna_peli(pelaaja)

        elif komento == "lopeta":
            print()
            print("Lopetetaan peli.")
            print()

        else:
            print()
            print("Virheellinen komento.")
            print()