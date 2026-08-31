#Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
#Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen
#samalla käyttäjälle, montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. 
#Kuha on alamittainen, jos sen pituus on alle 37 cm.

pituus = float(input("Anna kuhan pituus senttimetreinä: "))

if pituus < 37:
    puuttuu = 37 - pituus
    print("Kuha on alamittainen, laske se takaisin järveen.")
    print(f"Alimmasta sallitusta mitasta puuttuu {puuttuu} cm.")
else:
    print("Kuha on mitan mukainen, sen saa pyytää.")