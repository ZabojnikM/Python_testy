cislo = int(input("Zadej číslo : "))
if (cislo % 2 == 0):
    if (cislo % 4 == 0):
        print("Číslo je sudé a dělitelné čtyřmi !")
    else:
        print("Číslo je sudé !")
else:
    print("Číslo je liché !")