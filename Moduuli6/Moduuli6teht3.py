def main():
    maara = int(input("Anna muutettavat galloonat: "))
    print(f"Tulos: {litrat_galloonaan(maara)} l")


def litrat_galloonaan(gallon):
    return gallon * 3.785

main()

