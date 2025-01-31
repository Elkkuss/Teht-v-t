q = []
while True:
    luvut = input("Anna luku: ")
    if luvut == "":
        break
    else:
        q.append(float(luvut))

q.sort(reverse=True)

print("5 suurinta lukua ovat:")
for i in range(5):
    print(q[i], end=" ")

