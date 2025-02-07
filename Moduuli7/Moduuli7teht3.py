def main():
    kentät = {"EFHK": "Helsinki-Vantaan lentokenttä"}
    while True:
        print("Lisää uusi lentokenttä [L] tai hea olemassaoleva [H]. [Q] poistuaksesi")
        valinta = input("> ")
        if valinta.upper() == "L":
            print("Lisää lentokentän ICAO-koodi")
            uusi_icao = input("> ").upper()
            print("Lisää lentokentän nimi")
            uusi_nimi = input("> ")
            kentät.update({uusi_icao: uusi_nimi})
        elif valinta.upper() == "H":
            print("Kirjoita haettavan lentokentän ICAO-koodi")
            haettava_icao = input("> ").upper()
            if haettava_icao in kentät:
                print(kentät[haettava_icao])
            else: print("ICAO ei löydy")
        elif valinta.upper() == "Q":
            break
        else:
            print("Valinta ei 'L', 'H' Tai 'Q'")

main()


