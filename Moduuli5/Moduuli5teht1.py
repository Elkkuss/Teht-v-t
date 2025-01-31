import random
noppa = int(input("Anna arpakuutioiden määrä: "))
summa = 0
for luku in range(noppa):
    heitto = random.randint(1, 6)
    print(f"arpakuutio{luku+1}: {heitto}")
    summa += heitto
    print(f"Arpakuutioiden summa: {summa}.")


