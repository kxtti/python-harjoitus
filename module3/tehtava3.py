# Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden. 
# Ohjelma tulostaa suorakulmion piirin ja pinta-alan. Suorakulmion piiri 
# tarkoittaa sen neljän sivun yhteispituutta.

kanta_str = input("Anna suorakulmion kanta: ")
korkeus_str = input("Anna suorakulmion korkeus: ")

kanta = float(kanta_str)
korkeus = float(korkeus_str)

piiri = 2 * (kanta + korkeus)
pinta_ala = kanta * korkeus

print(f"Suorakulmion piiri on: {piiri}")
print(f"Suorakulmion pinta-ala on: {pinta_ala}")