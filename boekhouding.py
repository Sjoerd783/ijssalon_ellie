import helper
from presentatie import presenteer

def inkomsten():
    return {    
        "Aardbeien-ijs totaal": 1000,
        "Vanille-ijs totaal": 2000,
        "Chocolade-ijs totaal": 1500,
        "Waterijsjes totaal": 750
    }

inkomsten = inkomsten()

totaal_inkomsten = helper.som(inkomsten)

print(totaal_inkomsten)

totaal_bedrag = totaal_inkomsten  

presenteer(inkomsten, totaal_bedrag)

with open('boekhouding.csv', 'w', newline='') as csvfile:
    for key, value in inkomsten.items():
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([key,value])






    












    
    