from algemene_functies import mijn_functie_2 

def aanbieding_1():
    smaak = "aardbei"
    prijs = 4
    korting = 0.1
    korting = prijs * (1 - korting)
    return smaak, prijs, korting


smaak, prijs, korting = aanbieding_1()

reclame_tekst = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting} euro."
print(reclame_tekst)



def inkomsten_totaal():
    inkomsten = [220, 430, 125, 160, 205, 90, 345]
    btw = float(0.09)
    btw = sum(inkomsten)*btw
    totaal = sum(inkomsten) + btw
    return inkomsten, btw, totaal

inkomsten, btw, totaal = inkomsten_totaal()

inkomsten = f"Het totaal van alle inkomsten van deze week is {totaal} euro , waarover {btw} euro btw betaald dient te worden." 

print(inkomsten)



def laag_en_hoog():
    mijn_lijst=[220, 430, 125, 160, 205, 90, 345]
    laag=min(mijn_lijst) 
    hoog=max(mijn_lijst) 
    return laag, hoog

lh= laag_en_hoog()

print (lh)



def gemiddelde():
    mijn_lijst=[220, 430, 125, 160, 205, 90, 345]
    waarde = sum(mijn_lijst)
    aantal = len(mijn_lijst)
    gemiddelde = waarde/aantal
    return gemiddelde

gemiddelde = gemiddelde()
average = f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro."

print (average)



def meervoudig():
    invoer_lijst = [10, 5, 3, 2, 1, 2, 9]
    a = laag_en_hoog(invoer_lijst)
    return a

a = meervoudig()

print(a)


def combinatie():
    invoer_lijst_2 = meervoudig()




