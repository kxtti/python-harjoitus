# # while loop

# # User inputtii niin kauan kunnes user antaa "Quit" -stringin

# print("Komennot:\nJatka\nOhje\nLopeta\nSeis")

# user_command = input("Anna komento:")

# while user_command != "Lopeta":
#     # Iffejä joilla printataan valittu user command
#     if user_command == "Jatka":
#         print("Jatketaan seuraavaan looppiin!")
#     elif user_command == "Ohje":
#         print("Komennot:\nJatka\nOhje\nLopeta\nSeis")
#     elif user_command == "Seis":
#         print("Abort mission!")
#         break

#     user_command = input("Anna uusi komento:")

# print("End")


# LISTA JA FOR 

# autot = ["Audi", "Mersu", "Nissan"]
# autot.append("BMW")

# nimet = []

# nimet.append("Matti")

# print(nimet)

# #autot.append("Toyota")
# #autot.remove("Audi")

# print(autot)
# autot.sort()

# print(autot[2])
# print(autot[-2])
# print(autot[1:3])

# import random

# arpakuutiot = int(input("Anna arpakuutioiden määrä (tint): "))

# silmaluvut = 0

# for i in range(arpakuutiot):
#     silmaluvut += random.randint(1, 6)

# print(silmaluvut)



# MONIKKO JOUKKO JA SANAKIRJA
# Tuple, Set and dictionary

# LISTAT = []
# MONIKKO = ()
# JOUKKO {}
# SANAKIRJA {:}

# Tuple's are TOUGH
# viikonpaivat = ("MA", "TI", "KE", "TO")
# viikonpaivat = ("PE", "LA", "SU")

# def luvut(luku1, luku2):
#     eka = luku1
#     toka = luku2
#     return eka, toka

# noppa1, noppa2 = luvut (1,2)

# print(noppa1, noppa2)


#Set's are SPECIFIC




# FUNKTIOT
# import random

# heittojen_summa = 0

# def heita_noppaa(kerrat, tahkot=6):
#     summa = 0
    
#     for i in range(kerrat):
#         summa += random.randint(1,tahkot)
#     return summa

# heittojen_summa = heita_noppaa(4, 21)

# print(f"Heittojen summa: {heittojen_summa}")