nimi = input("Anna pelaajan nimi: ")
ikä = int(input("Anna pelaajan ikä: "))
print("Pelaajan nimi:", nimi)
print("Pelaajan ikä:", ikä)

if ikä < 12:
    print("Olet liian nuori pelaamaan peliä. Peli suljetaan.")
else:
    print("Tervetuloa " + nimi + "!")


    komento = ""
    while komento != "lopeta":
        print("--- PÄÄVALIKKO ---")
        print("Aloita - Aloittaa pelin")
        print("Pisteet - Näyttää pisteet")
        print("Lopeta - Lopettaa ohjelman")
 
        komento = input("Anna komento: ").lower()
 
        if komento == "aloita":
            print("Peli alkaa.")
        elif komento == "pisteet":
            print("Pisteesi ovat: 0")
        elif komento == "lopeta":
            print("Lopetetaan peli.")
        else:
            print("Virheellinen valinta.")