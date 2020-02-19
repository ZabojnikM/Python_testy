# Zadání sudoku
from timeit import default_timer as timer


global Zadani
Zadani = [[7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]]

Vysledek = [[7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]]
 



def krok_vpred(rada_krok,sloupec_krok):
    if sloupec_krok < 8:
        sloupec_krok += 1
    else:
        sloupec_krok = 0
        rada_krok +=1
        
    return(rada_krok,sloupec_krok)

def krok_vzad(rada_krok,sloupec_krok):
    if sloupec_krok > 0:
        sloupec_krok -= 1
    else:
        sloupec_krok = 8
        rada_krok -=1
    return(rada_krok,sloupec_krok)

def test_cisla(rada_testuj,sloupec_testuj,cislo):

    for x in range(9):
        if Vysledek[x][sloupec_testuj] == cislo or Vysledek[rada_testuj][x] == cislo :
            return(False)

    

    ctverec_rada = (rada_testuj // 3) *3
    ctverec_sloupec = (sloupec_testuj // 3) *3
    for rada in range(ctverec_rada,ctverec_rada+3):
        if rada != rada_testuj:
            for sloupec in range(ctverec_sloupec,ctverec_sloupec+3):
                if Vysledek[rada][sloupec] == cislo:
                    return(False)   
    

    return(True)



        
rada = 0
sloupec = 0
zpet = False
konec = False
start = timer()
while konec != True:        
    
   
    if Zadani[rada][sloupec] == 0:
        test = False
        test_cislo = Vysledek[rada][sloupec]
        while test == False :
            test_cislo +=  1
            test = test_cisla(rada,sloupec,test_cislo)
            

            
        #print(rada,sloupec,test_cislo)
        if test_cislo > 9:
            zpet = True
            Vysledek[rada][sloupec] = 0
            
        else:
            zpet = False
            Vysledek[rada][sloupec] = test_cislo
            
        
    else:
        Vysledek[rada][sloupec] = Zadani[rada][sloupec]
        
    
    if zpet == True:
        rada,sloupec = krok_vzad(rada,sloupec)
    else:
        rada,sloupec = krok_vpred(rada,sloupec)
 
    if rada > 7 and sloupec > 7:
        konec = True
        
    if rada == 0 and sloupec == 0:
        konec = True
    
  
    
end = timer()
print(end - start)    
    
    
    
    
"""while rada + sloupec > 0 :
    rada,sloupec = krok_vzad(rada,sloupec)
    print(rada,sloupec)"""

"""for rada in range(9):
    radek_print = ""
    for sloupec in range(9):
        radek_print = radek_print + " " + str(Zadani[rada][sloupec])
    print (radek_print)"""

print()

for rada in range(9):
    if rada % 3 == 0 and rada != 0:
        print("- - - - - - - - - - - - - ")
    for sloupec in range(9):
        if sloupec % 3 == 0 and sloupec != 0:
            print(" | ", end="")
                
        if sloupec == 8:
            print(str(Vysledek[rada][sloupec]))
        else:
            print(str(Vysledek[rada][sloupec]) + " ", end="")
      
    

