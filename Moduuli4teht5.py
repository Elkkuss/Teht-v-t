oikeat = "python"
oikeass = "rules"
yritykset = 0
while yritykset < 5:
    tunnus = input("Syötä käyttäjätunnus: ")
    salasana = input("Syötä salasana: ")
    if tunnus == oikeat and salasana == oikeass:
        print("Tervetuloa.")
        break
    else:
        yritykset += 1
        if yritykset < 5:
            print(f"Väärä tunnus tai salasana.")
        else:
            print("Pääsy evätty.")
