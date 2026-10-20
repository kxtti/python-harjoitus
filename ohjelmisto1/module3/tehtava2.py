# Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.

import math

sade_str = input("Anna ympyrän säde: ")
sade = float(sade_str)
pinta_ala = math.pi * sade ** 2

print(f"Ympyrän pinta-ala on {pinta_ala:.2f}")