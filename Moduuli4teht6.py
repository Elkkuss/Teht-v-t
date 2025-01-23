import random
monta = int(input("Anna pisteiden määrä: "))
o = 0
for _ in range(monta):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        o += 1
likiarvo = 4 * o / monta
print(f"Piin likiarvo on noin: {likiarvo}")


