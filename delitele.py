
#Komentář pro test github
#Test 2

while True:
    while True:
        cislo = input("Zadej celé kladné číslo : ")
        if (str.isdigit(cislo) == True):
            break
        else:
            print(cislo + " není správné číslo !")

    print("Delitelé čísla " + str(cislo) + " jsou :",end =" ")

    cislo = int(cislo)
    for x in range(cislo + 1,1,-1):
        if(cislo % x == 0):
            print(str(x),end = " ")

    ano = input("\nChceš zadat další číslo ? A/N ")
    if (ano != "a" and ano != "A"):
       break
    