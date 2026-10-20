import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, muutos):
        uusi_nopeus = self.nopeus + muutos
        if uusi_nopeus > self.huippunopeus:
            uusi_nopeus = self.huippunopeus
        if uusi_nopeus < 0:
            uusi_nopeus = 0
        self.nopeus = uusi_nopeus

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit


class Kilpailu:
    def __init__(self, nimi, kilometrit, autot):
        self.nimi = nimi
        self.kilometrit = kilometrit
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdytä(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\n=== {self.nimi} - tilanne ===")
        print(f"{'Rekisteritunnus':<16}{'Huippunopeus':<15}{'Nopeus':<10}{'Matka':<10}")
        print("-" * 51)
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<16}{auto.huippunopeus:<15}"
                  f"{auto.nopeus:<10}{round(auto.matka):<10}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.kilometrit:
                return True
        return False


# Pääohjelma / Main program

# Luodaan kymmenen auton lista
autot = []
for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunteja_kulunut = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunteja_kulunut += 1

    if tunteja_kulunut % 10 == 0:
        kilpailu.tulosta_tilanne()

# Tulostetaan lopputilanne kilpailun päätyttyä
print("\nKilpailu on ohi!")
kilpailu.tulosta_tilanne()