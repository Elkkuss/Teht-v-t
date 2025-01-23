import random
luku = random.randint(1,10)
yritykset = 0
while True:
    try:
        yritys = int(input("Arvaa lukua välillä 1-10: "))
        yritykset += 1
        if yritys < luku:
            print("Liian pieni arvaus.")
        elif yritys > luku:
            print("Liian suuri arvaus.")
        else:
            print(f"Hienoa! Arvasit luvun {luku} oikein {yritykset} arvauksella.")
    except ValueError:
        print("Syötä kokonaisluku.")
