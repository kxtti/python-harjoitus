""" Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.
Vihje: tutustu random.randint()-funktion käyttöön. """

import random

numero1 = random.randint(0, 9)
numero2 = random.randint(0, 9)
numero3 = random.randint(0, 9)

numero4 = random.randint(1, 6)
numero5 = random.randint(1, 6)
numero6 = random.randint(1, 6)
numero7 = random.randint(1, 6)

print(f"Kolmenumeroinen koodi: {numero1}{numero2}{numero3}")
print(f"Nelinumeroinen koodi: {numero4}{numero5}{numero6}{numero7}")