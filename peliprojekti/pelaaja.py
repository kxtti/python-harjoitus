class Pelaaja:
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.kierrätetyt = []
        self.sijainti = sijainti

    def kierrätä(self, roska):
        print("Löysit:", roska.nimi)

        vastaus = input("Mihin astiaan se kuuluu? (lasijäte/muovijäte/metallijäte/paperijäte/elektroniikkajäte/biojäte/pahvijäte): ").lower()
        if vastaus == roska.oikea_astia:
            print("Oikein! Sait yhden pisteen.")
            self.kierrätetyt.append(roska.nimi)
            return True
        else:
            print("Väärin! Peli päättyy.")
            return False

    def näytä_kierrätetyt(self):
        print("Olet kierrättänyt:")

        if len(self.kierrätetyt) == 0:
            print("Et ole kierrättänyt vielä mitään.")
        else:
            for roska in self.kierrätetyt:
                print("-", roska)

    def näytä_pisteet(self):
        print("Pisteesi:", len(self.kierrätetyt))

    def vaihda_sijaintia(self, paikat):
        print("Nykyinen sijaintisi:", self.sijainti.nimi)

        print("Minne haluat mennä?")
        for paikka in paikat:
            print(paikka.nimi)

        valinta = input("Kirjoita sijainti:").lower()

        löytyi = False
        for paikka in paikat:
            if paikka.nimi.lower() == valinta:
                self.sijainti = paikka
                löytyi = True

        if not löytyi:
            print("Virheellinen sijainti.")