puoli = input("Sukupuoli: ")
hemo = int(input("Anna Hemoglobiiniarvo: "))
if puoli == "Nainen":
    if hemo < 117:
        print("Hemoglobiini alhainen. ")
    elif 117 <= hemo <= 175:
        print("Hemoglobiini on normaali. ")
    else:
        print("Hemoglobiini on korkea.")
elif puoli == "Mies":
    if hemo < 134:
        print("Hemoglobiini alhainen. ")
    elif 134 <= hemo <= 195:
        print("Hemoglobiini  on normaali.")
    else:
        print("Hemoglobiini on korkea.")
else:
    print("Väärä sukupuoli. ")




