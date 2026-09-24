# # Periytyminen ja kertaus kokeeseen

# # PERIYTYMINEN ESIMERKKI
# # 1. Luo varusmiesluokka, jolla on nimi, sukunimi
# # Luo sille metodiksi ilmoita tiedot; joka printtaa nimen ja sukunimen

# class Varusmies():
#     def __init__(self, nimi, sukunimi):
#         self.nimi = nimi
#         self.sukunimi = sukunimi

#     def ilmoita_tiedot(self):
#         print(f"{self.nimi} {self.sukunimi}")

# class Miehistö(Varusmies):
#     def __init__(self, nimi, sukunimi, arvo="Sotamies"):
#         super().__init__(nimi, sukunimi)
#         self.arvo = arvo

#     def ilmoita_tiedot(self):
#         super().ilmoita_tiedot()
#         print(f"{self.arvo}")

# class Henkilökunta(Miehistö):
#     def __init__(self, nimi, sukunimi, arvo, tehtävä):
#         super().__init__(nimi, sukunimi, arvo)
#         self.tehtävä = tehtävä

#     def ilmoita_tiedot(self):
#         print("Henkilökunta: ")
#         super().ilmoita_tiedot()
#         print(f"{self.tehtävä}")

# # varusmies1 = Varusmies(input("Anna etunimesi: "),input("Anna sukunimesi: "))
# # varusmies1.ilmoita_tiedot()

# miehistö1 = Miehistö(input("Anna etunimesi: "),input("Anna sukunimesi: "),input("Anna sotilasarvosi: "))
# miehistö1.ilmoita_tiedot()

# print()

# henk1 = Henkilökunta("Sofia", "Sotilas", "Vääpeli", "Logistiikka")
# henk1.ilmoita_tiedot()



# MONIPERINTÄ

class Isä():
    def __init__(self, auto):
        self.auto = auto

class Äiti():
    def __init__(self, linna):
        self.linna = linna

class Minä(Isä, Äiti):
    def __init__(self, auto, linna, persoonallisuus):
        Isä.__init__(self, auto)
        Äiti.__init__(self, linna)
        self.persoonallisuus = persoonallisuus

minä = Minä("Volkswagen", "Suomenlinna", "Rohkea")

print(minä.auto)
print(minä.linna)
print(minä.persoonallisuus)