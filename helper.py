def onderstreep(tekst=""):    
    uit = []    
    uit.append(tekst)    
    uit.append(len(tekst) * "=")    
    return uit


def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()


def fooi_pp(bedrag, personen):    
    try:         
        bedrag_pp = bedrag/personen    
    except:         
        bedrag_pp = "??"    
    return f"Het bedrag per persoon is {bedrag_pp} euro"


def onderstreep(tekst = ""):
    uit = []
    uit.append(tekst)
    uit.append(len(tekst) * "=")
    return uit

from helper import onderstreep

uitvoer = onderstreep("AANBIEDING")
uitvoer.append("Aardbeienijs, emmertje van 5 liter: 5 euro")
uitvoer.append("Slagroom, spuitbus van 1 liter: 2 euro")



def som(dictionary):
    totaal = 0
    for value in dictionary.values():
        totaal += value
    return totaal





    
    

    
