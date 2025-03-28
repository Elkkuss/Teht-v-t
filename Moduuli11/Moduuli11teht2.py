class Auto:

    def __init__(self, rekkari, huippu):
        self.rekkari = rekkari
        self.huippu = huippu
        self.nopeus = 0
        self.mittari = 0

    def kiihdyta(self, nopeus):
        if 0 <= nopeus <= self.huippu:
            self.nopeus = nopeus
        else:
            print("Nopeus ei voi ylittää huippunopeutta!")

    def aja(self, tunnit):
        self.mittari += self.nopeus * tunnit

class Sahkoauto(Auto):
    def __init__(self, rekkari, huippu, akku):
        self.akku = akku
        super(). __init__(rekkari, huippu)

class Polttomoottoriauto(Auto):
    def __init__(self, rekkari, huippu, tankki):
        self.tankki = tankki
        super(). __init__(rekkari, huippu)

tesla = Sahkoauto("ABC-123", 180, 52.5)
mersu = Polttomoottoriauto("CBA-321", 165, 32.3)

tesla.kiihdyta(120)
mersu.kiihdyta(150)

tesla.aja(3)
mersu.aja(3)

print(f"Teslan mittarilukema: {tesla.mittari} km")
print(f"Mersun mittarilukema: {mersu.mittari} km")



