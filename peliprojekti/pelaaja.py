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

        vastaus = input("Mihin astiaan se kuuluu? (lasijäte/muovijäte/metallijäte/paperijäte/elektroniikkajäte/biojäte/pahvijäte): ").lower()
        if vastaus == roska.oikea_astia:
            print()
            print("Oikein! Sait yhden pisteen.")
            print()
            self.kierrätetyt.append(roska.nimi)
            return True
        else:
            print()
            print("Väärin! Peli päättyy.")
            print()
            return False

# Näyttää kaikki siihen mennessä kierrätetyt
    def näytä_kierrätetyt(self):
        print()
        print("Olet kierrättänyt:")

        if len(self.kierrätetyt) == 0:
            print()
            print("Et ole kierrättänyt vielä mitään.")
            print()
        else:
            for roska in self.kierrätetyt:
                print("-", roska)

# Näyttää pisteet oikein kierrätetyistä roskista
    def näytä_pisteet(self):
        print()
        print("Pisteesi:", len(self.kierrätetyt))
        print()

# Antaa pelaajan vaihtaa nykyistä sijaintia
    def vaihda_sijaintia(self, paikat):
        print()
        print("Nykyinen sijaintisi:", self.sijainti.nimi)
        print()

        print("Minne haluat mennä?")
        print()

# Tulostetaan kaikki sijainnit
        for paikka in paikat:
            print(paikka.nimi)
        print()
        valinta = input("Kirjoita sijainti:").lower()

        löytyi = False

# Etsii sijainnin paikkalistasta
        for paikka in paikat:
            if paikka.nimi.lower() == valinta:
                self.sijainti = paikka
                löytyi = True

        if not löytyi:
            print()
            print("Virheellinen sijainti.")
            print()