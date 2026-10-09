class Pelaaja:

    # Pelaajalle tallennetaan nimi, kierrätetyt roskat ja sijainti
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.kierrätetyt = []
        self.sijainti = sijainti


    # Kysyy minne roska kuuluu ja tarkistaa onko vastaus oikein
    def kierrätä(self, roska):
        print()
        print("Löysit:", roska.nimi)
        print()

        # Pelissä olevat jäteastiat
        astiat = [
            "lasijäte",
            "muovijäte",
            "metallijäte",
            "paperijäte",
            "elektroniikkajäte",
            "biojäte",
            "pahvijäte"
        ]

        # Kysytään vastausta kunnes pelaaja antaa oikean jäteastian nimen
        while True:
            vastaus = input(
                "Mihin astiaan se kuuluu? "
                "(lasijäte/muovijäte/metallijäte/paperijäte/"
                "elektroniikkajäte/biojäte/pahvijäte): "
            ).lower()

            # Tarkistetaan onko kirjoitettu jäteastia olemassa
            if vastaus not in astiat:
                print()
                print("Tuollaista jäteastiaa ei ole.")
                print("Yritä uudelleen.")
                print()

            # Oikea jäteastia
            elif vastaus == roska.oikea_astia:
                print()
                print("Oikein! Sait yhden pisteen.")
                print()

                self.kierrätetyt.append(roska.nimi)

                return True

            # Olemassa oleva, mutta väärä jäteastia
            else:
                print()
                print("Väärin! Peli päättyy.")
                print()

                return False


    # Näyttää kaikki siihen mennessä kierrätetyt
    def näytä_kierrätetyt(self):
        print()
        print("--- INVENTAARIO ---")
        print()

        if len(self.kierrätetyt) == 0:
            print("Et ole kierrättänyt vielä mitään.")
            print()

        else:
            for roska in self.kierrätetyt:
                print("-", roska)

            print()


    # Näyttää pisteet oikein kierrätetyistä roskista
    def näytä_pisteet(self):
        print()
        print("--- PISTEET ---")
        print()
        print("Pisteesi:", len(self.kierrätetyt))
        print()


    # Antaa pelaajan vaihtaa nykyistä sijaintia
    def vaihda_sijaintia(self, paikat):
        print()
        print("--- LIIKKUMINEN ---")
        print()
        print("Nykyinen sijaintisi:", self.sijainti.nimi)
        print()

        print("Minne haluat mennä?")
        print()

        # Tulostetaan kaikki reitin sijainnit
        for paikka in paikat:
            print("-", paikka.nimi)

        print()

        valinta = input("Kirjoita sijainti: ").lower()

        löytyi = False

        # Etsii sijainnin paikkalistasta
        for paikka in paikat:
            if paikka.nimi.lower() == valinta:
                self.sijainti = paikka
                löytyi = True

        print()

        if löytyi:
            print("Siirryit paikkaan:", self.sijainti.nimi)
            print()

        else:
            print("Virheellinen sijainti.")
            print()