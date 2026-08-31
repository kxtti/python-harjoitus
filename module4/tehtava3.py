#Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
#Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

sukupuoli = input("Kerro sukupuolesi: ").lower()
hemoglobiiniarvo = float(input("Anna hemoglobiiniarvosi (g/l): "))

if sukupuoli == "nainen":
    if hemoglobiiniarvo < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemoglobiiniarvo <= 175:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")
elif sukupuoli == "mies":
    if hemoglobiiniarvo < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemoglobiiniarvo <= 195:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")
else:
    print("Virheellinen sukupuoli.")