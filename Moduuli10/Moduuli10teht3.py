class Hissi:
    def __init__(self, alin, ylin, kerros=1):
        self.alin = alin
        self.ylin = ylin
        self.kerros = self.alin

    def siirry_kerrokseen(self, kohde):
        if kohde > self.kerros:
            for i in range(abs(kohde - self.kerros)):
                self.kerros_ylos()
        else:
            for i in range(abs(kohde - self.kerros)):
                self.kerros_alas()

    def kerros_ylos(self):
        self.kerros += 1
        print(self.kerros, end=" ")

    def kerros_alas(self):
        self.kerros -= 1
        print(self.kerros, end=" ")


class Talo:
    hissit_lista = []

    def __init__(self, alin, ylin, hissit_lkm):
        self.alin = alin
        self.ylin = ylin
        self.hissit_lkm = hissit_lkm

        for i in range(hissit_lkm):
            self.hissit_lista.append(Hissi(self.alin, self.ylin))

    def hissilla(self, hissi, kohde):
        self.hissit_lista[hissi - 1].siirry_kerrokseen(kohde)

    def palohalytys(self):
        print("Palohalytys")
        for hissi in self.hissit_lista:
            hissi.siirry_kerrokseen(self.alin)

t = Talo(1, 10, 3)

t.hissilla(1, 4)

luku = 1
for hissi in Talo.hissit_lista:
    print(f"Hissi {luku} - kerros: {hissi.kerros}")
    luku += 1

t.palohalytys()

for hissi in Talo.hissit_lista:
    print(f"Hissi {luku} - kerros: {hissi.kerros}")
    luku += 1