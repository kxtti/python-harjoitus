luku = int(input("Anna kokonaisluku: "))

on_alkuluku = True

for i in range(2, luku):
    if luku % i == 0:
        on_alkuluku = False

if on_alkuluku:
    print(luku, "on alkuluku")
else:
    print(luku, "ei ole alkuluku")