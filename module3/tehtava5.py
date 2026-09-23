"""Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä,
nauloina ja luoteina. Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä 
ilmoittaa tuloksen käyttäjälle.
Yksi leiviskä on 20 naulaa.
Yksi naula on 32 luotia.
Yksi luoti on 13,3 grammaa.
Esimerkki ohjelman toiminnasta:

Anna leiviskät.
3

Anna naulat.
9

Anna luodit.
13.5

Massa nykymittojen mukaan:
29 kilogrammaa ja 545.95 grammaa. """

leiviskat = float(input("Anna leiviskät\n"))
naulat = float(input("\nAnna naulat\n"))
luodit = float(input("\nAnna luodit\n"))

luoteja_yhteensa = leiviskat * 20 * 32 + naulat * 32 + luodit
grammoja_yhteensa = luoteja_yhteensa * 13.3

kilogrammat = int(grammoja_yhteensa // 1000)
grammat = grammoja_yhteensa - kilogrammat * 1000

print("\nMassa nykymittojen mukaan:")
print(f"{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.")