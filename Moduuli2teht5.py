leiviskä_str = input("Anna leiviskät: ")
naula_str = input(" Anna naulat: ")
luoti_str = input(" Anna luodit: ")
leiviskä = float(leiviskä_str)
naula = float(naula_str)
luoti = float(luoti_str)
luoteja = (leiviskä * 20 * 32) + (naula * 32) + luoti
grammat = luoteja * 13.3
kilot = grammat // 1000
grammat2 = grammat % 1000
print(f"Massasi nykymittojen mukaan {kilot} kilogrammaa ja {grammat2} grammaa.")

