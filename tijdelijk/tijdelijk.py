prijzen = {
    "aardbei" : "3", 
    "vanille" : "4", 
    "chocolade" : "5"
}

aanbieding = int(prijzen["aardbei"])*0.8
reclame_tekst = (f"Vandaag in de aanbieding : aardbeien-ijs, 1 liter – slechts € {aanbieding}")
reclame_tekst2 = reclame_tekst[:66]
reclame_tekst3 = (reclame_tekst2).upper()
reclame_tekst4 = reclame_tekst3.split(" ")
for el in reclame_tekst4:
    if len(el)<4:
        print((el).lower())
    else:
        print(el)








    
