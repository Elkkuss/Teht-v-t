def main():
    print("Syötä nimä. tyhjä kun valmis")
    nimi = set()
    while True:
        set_len = len(nimi)
        user_input = input("> ").title()
        if user_input == "":
            break
        else:
            if user_input not in nimi:
                print("Uusi nimi")
                nimi.add(user_input)
            else:
                print("Nimi on jo syötetty")
    for nimet in nimi:
        print(nimet, end=" ")


main()

