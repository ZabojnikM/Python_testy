import time

jmeno = input("Zadej své jméno :")
vek = int(input("Zadej svůj věk :"))
aktualnirok = time.localtime()[0]
stolet = aktualnirok + 100 - vek
narozen = aktualnirok - vek

print("V roce " +str(stolet) + " ti bude sto let .")
print("Narodil jsi se v roce : " + str(narozen))