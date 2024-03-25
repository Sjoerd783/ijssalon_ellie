import helper 
import presentatie

def inkomsten():
    return {    
        "Aardbeien-ijs totaal": 1000,
        "Vanille-ijs totaal": 1000,
        "Chocolade-ijs totaal": 2000,
        "Waterijsjes totaal": 750
    }

inkomsten = inkomsten()


totaal_inkomsten = helper.som(inkomsten)

print(totaal_inkomsten)


    












    
    