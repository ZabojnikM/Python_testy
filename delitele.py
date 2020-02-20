
#Komentář pro test github
#Test 2
#Test pull reqest

while True:
    while True:
        cislo = input("Zadej celé kladné číslo : ")
        if (str.isdigit(cislo) == True):
            break
        else:
            print(cislo + " není správné číslo !")

    výsledek = "\nDelitelé čísla " + str(cislo) + " jsou : "

    cislo = int(cislo)
    procenta = int(cislo)
    aktproc = 1
    for x in range(cislo + 1,1,-1):
        if(x < procenta):
            print("\rProceno prohledaných čísel : ",aktproc,"%",end =" ")
            aktproc += 1
            procenta = procenta - cislo/100
        if(cislo % x == 0):
            výsledek += str(x) + " "

    print(výsledek)
    ano = input("Chceš zadat další číslo ? A/N ")
    if (ano != "a" and ano != "A"):
       break
    