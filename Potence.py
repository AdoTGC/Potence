#Definiramo spremenljivke
stevilo1 = 0
stevilo2 = 0

osnova = 0
eksponent = 0
vrednostPotence = 0

kumulativnaVsota = 0

stPravilnihParov = 0
stNepravilnihParov = 0

#Funkcija, ki nam pove katero je večje izmed 2 števil (imamo 2 argumenta, in pogledamo če je prvo število (argument) večji in ga vrnemo, če ne, vrnemo drugega.
def vecjeStevilo(st1, st2):
    if st1 > st2:
        return st1
    else:
        return st2

#Enaka funkcija kot zgoraj, le da tokrat nam vrne manjše število
def manjseStevilo(st1, st2):
    if st1 < st2:
        return st1
    else:
        return st2

#Zanka, ki se ponavlja dokler je kumulativna vsota potenc manjša od 1000
while kumulativnaVsota < 1000:
    #dobijemo par števil, ki ga uporabnik vnese in ga vpišemo v spremenljivko
    stevilo1 = int(input("Vnesite število med 2 in 8:"))
    stevilo2 = int(input("Vnesite 2. število med 2 in 8:"))

    #Preverjamo če je katero od števil izven dovoljenega območja in oseba mora vnesti nov par števil. To ponavljamo dokler ne bo par pravilen
    while stevilo1 < 2 or stevilo1 > 8 or stevilo2 < 2 or stevilo2 > 8:
        #K številu nepravilnih parov dodamo 1
        stNepravilnihParov = stNepravilnihParov + 1
        #Opozorimo uporabnika
        print("Vneseni par števil je neveljaven!")
        #Še enkrat uporabniku ponudimo, da vpiše števili
        stevilo1 = int(input("Vnesite število med 2 in 8:"))
        stevilo2 = int(input("Vnesite 2. število med 2 in 8:"))
        
    #Dodamo 1 k številu pravilnih parov, saj vemo, da se ta ukaz ne bo izvedel dokler par ne bo pravilen
    stPravilnihParov = stPravilnihParov + 1

    #V spremenljivko 'osnova' vpišemo večje izmed števil
    osnova = vecjeStevilo(stevilo1, stevilo2)
    # V spremenljivko 'eksponent' vpišemo manjše izmed števil
    eksponent = manjseStevilo(stevilo1, stevilo2)
    #V spremenljivko 'vrednostPotence' vpišemo vrednost osnove(če bi bila vrednost spremenljivke 'vrednostPotence' 0, bi rezultat bil nepravilen)
    vrednostPotence = osnova

    #Ponovimo zanko tolikokrat, kolikšna je vrednost eksponenta, le enkrat manj, ker imamo v rezultatu že vpisan 1. produkt
    for i in range(eksponent - 1):
        #Množimo vrednost v spremenljivki 'vrednostPotence' z osnovo in spet vpisujemo v 'vrednostPotence'
        vrednostPotence = vrednostPotence * osnova
    #K kumulativni vsoti dodamo vrednost potence
    kumulativnaVsota = kumulativnaVsota + vrednostPotence
    #Izpišemo vrednost potence
    print("Potenca z osnovo " + str(osnova) + " in eksponentom " + str(eksponent) + " znaša " + str(vrednostPotence))
    
#Ta dva ukaza spodaj se ne bosta zagnala dokler kumulativna vsota ne bo večja kot 1000
#Izpišemo koliko pravilnih in nepravilnih parov števil je uporabnik vnesel
print("Podali ste " + str(stPravilnihParov) + " pravilenih parov števil, katerih skupna vsota potenc znaša " + str(kumulativnaVsota))
print("Napravili ste " + str(stNepravilnihParov) + " nepravilnaih parov števil")
