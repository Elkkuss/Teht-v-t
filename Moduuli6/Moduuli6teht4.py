def laske_summa(luvut):
    summa = 0
    for luku in luvut:
        summa += luku
    return summa


luvut = [2,12,7,32,4]

summa = laske_summa(luvut)
print('Summa on ' + str(summa))


