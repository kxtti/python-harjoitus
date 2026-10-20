"""Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes 
tämä syöttää tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa
saaduista luvuista pienimmän ja suurimman."""



luku_str = input("Anna luku: ")

if luku_str != "":
    luku = float(luku_str)
    pienin = luku
    suurin = luku

    luku_str = input("Anna luku: ")

    while luku_str != "":
        luku = float(luku_str)

        if luku < pienin:
            pienin = luku
        if luku > suurin:
            suurin = luku

        luku_str = input("Anna luku: ")

    print(f"Pienin luku: {pienin}")
    print(f"Suurin luku: {suurin}")
else:
    print("Lukuja ei syötetty.")