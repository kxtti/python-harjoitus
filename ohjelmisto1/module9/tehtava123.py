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


auto = Auto("ABC-123", 142)

print(auto.rekisteritunnus)
print(auto.huippunopeus)
print(auto.nopeus)
print(auto.matka)

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
print(auto.nopeus)

auto.kiihdytä(-200)
print(auto.nopeus)