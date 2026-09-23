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


autot = []
for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))

voittaja_löytyi = False
while not voittaja_löytyi:
    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdytä(muutos)
        auto.kulje(1)

    for auto in autot:
        if auto.matka >= 10000:
            voittaja_löytyi = True

print(f"{'Rekisteritunnus':<16}{'Huippunopeus':<15}{'Nopeus':<10}{'Matka':<10}")
print("-" * 51)
for auto in autot:
    print(f"{auto.rekisteritunnus:<16}{auto.huippunopeus:<15}"
          f"{auto.nopeus:<10}{round(auto.matka):<10}")