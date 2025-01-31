from math import pi

def main():
    print(" Tämä ohjelma laskee pitsojen hinnan. ")

    pizzahalk = float(input("Pizza 1 halkaisija (cm): "))
    pizzahin = float(input("Pizza 1 hinta (€): "))

    pizza2halk = float(input("Pizza 2 halkaisija (cm): "))
    pizza2hin = float(input("Pizza 2 hinta (€): "))

    piz1_hinta = pizza_lasku(pizzahalk, pizzahin)
    piz2_hinta = pizza_lasku(pizza2halk, pizza2hin)

    print(f"\nPizza 1 hinta neliömetriltä: {str(piz1_hinta)[0:5]} €/m²")
    print(f"Pizza 2 hinta neliömetriltä: {str(piz2_hinta)[0:5]} €/m²")
    if piz1_hinta <piz2_hinta:
        print("Pizza 1 on halvempi per m²")
    elif piz1_hinta == piz2_hinta:
        print("Pizzat ovat saman hintaisia per m²")
    else:
        print("Pizza 2 on halvempi per m²")


def pizza_lasku(halkaisija, hinta):
    pinta = ((pi / 4) * halkaisija**2) * 0.0001
    return hinta / pinta

main()

