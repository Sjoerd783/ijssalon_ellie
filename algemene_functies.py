def mijn_functie_1(a):
    argumenten = [2, 4, 10, 12]
    return argumenten[a] ** 2


teruggeefwaarde = mijn_functie_1(1)

print(teruggeefwaarde)

def mijn_functie_2(a):
    argument1 = [12, 12, 10, 100]
    argument2 = [3, 2, 5, 20]
    return argument1[a] + argument2[a], argument1[a] - argument2[a], argument1[a] * argument2[a], argument1[a] / argument2[a]

teruggeefwaarde = mijn_functie_2(1)
print(teruggeefwaarde)