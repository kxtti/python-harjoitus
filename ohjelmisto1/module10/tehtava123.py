class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros

    def kerros_ylös(self):
        if self.kerros < self.ylin_kerros:
            self.kerros += 1
        print(f"Hissi on kerroksessa {self.kerros}")

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
        print(f"Hissi on kerroksessa {self.kerros}")

    def siirry_kerrokseen(self, kerros):
        while self.kerros < kerros:
            self.kerros_ylös()
        while self.kerros > kerros:
            self.kerros_alas()


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_määrä):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []
        for i in range(hissien_määrä):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))

    def aja_hissiä(self, hissin_numero, kerros):
        hissi = self.hissit[hissin_numero]
        hissi.siirry_kerrokseen(kerros)

    def palohälytys(self):
        print("Palohälytys! Kaikki hissit siirtyvät pohjakerrokseen.")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin_kerros)


# Pääohjelma / Main program
talo = Talo(0, 10, 3)

talo.aja_hissiä(0, 5)
talo.aja_hissiä(1, 8)
talo.aja_hissiä(2, 3)

talo.palohälytys()