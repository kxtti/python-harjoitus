# MODULE 9 CLASS, OBJECT AND CONSTRUCTOR

class Hero:
    sankarien_määrä = 0
    

    def __init__(self, nimi, tyyppi, voima, aseaani, huudahdus="Hei!"):
        self.nimi = nimi
        self.tyyppi = tyyppi
        self.voima = voima
        self.huudahdus = huudahdus
        self.aseaani = aseaani
        Hero.sankarien_määrä = Hero.sankarien_määrä + 1

    def huuda(self, kerrat=1):
        for i in range(kerrat):
            print(f"{self.huudahdus}")

    def ase(self):
        print(self.aseaani)


hero1 = Hero("Reinhardt", "Tankki", "Voimakas", "BONK", "AAARGH")
hero2 = Hero("Tracer", "Vahingontekijä", "Nopea", "Bäng")
hero3 = Hero("Blabla", "Tukija", "Parannus", "Viuh")

print(f"{hero1.nimi} on {hero1.tyyppi} ja hän on {hero1.voima}, hän sanoo {hero1.huudahdus}")
print(f"{hero2.nimi} on {hero2.tyyppi} ja hän on {hero2.voima}, hän sanoo {hero2.huudahdus}")

hero1.huuda()
hero1.ase()

hero2.huuda(2)
hero2.ase()

print(f"Sankarien määrä joukkueessa: {Hero.sankarien_määrä}")