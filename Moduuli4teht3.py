
luvut = []

while True:
    numero = input("Syötä luku: ")

    if numero == "":
        break

    try:
        luku = float(numero)
        luvut.append(luku)
    except ValueError:
        print("Virheellinen syöte, yritä uudelleen.")

if luvut:
    pienin = min(luvut)
    suurin = max(luvut)
    print(f"Pienin luku on {pienin} ja suurin luku on {suurin}.")

