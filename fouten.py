import 

def discriminant(a,b,c):
    try:
        D1 = (-b + math.sqrt(b**2 - 4*a*c))/(2 * a)
        D2 = (-b - math.sqrt(b**2 - 4*a*c))/(2 * a)

    except:
        D1 = "geen oplossing"
        D2 = "geen oplossing"

    uitvoer=[D1,D2]
    return uitvoer

print("Voor de formule ax^2+bx+c, geef a,b en c:")

a=int(input("Wat is a?"))
b=int(input("Wat is b?"))
c=int(input("Wat is c?"))

uitkomst=discriminant(a,b,c)

D1=uitkomst[0]
D2=uitkomst[1]

print(f"De discriminanten voor {a}x^2+{b}x+{c} zijn:{D1} en {D2}")

print("Voor de formule ax^2 + bx + c, geef a, b en c:")


