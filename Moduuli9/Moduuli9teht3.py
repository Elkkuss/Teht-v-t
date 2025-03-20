class Auto:
    def __init__(self, huippunopeus):
        self.nopeus = 0
        self.huippunopeus = huippunopeus
        self.matka = 0

    def kiihdytä(self, kiihdytys):
        vauhti = self.nopeus + kiihdytys

        if vauhti > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif vauhti < 0:
            self.nopeus = 0
        else:
            self.nopeus = vauhti

    def kulje(self, tuntia):
        matka = self.nopeus * tuntia
        self.matka += matka

volvo = Auto(142)

volvo.kiihdytä(30)
volvo.kiihdytä(70)
volvo.kiihdytä(50)

print(f"Auton nopeus kiihdytyksen jälkeen: {volvo.nopeus} km/h")

volvo.kulje(1.5)
print(f"Auto kulki {volvo.matka} km kiihdytyksen aikana.")

volvo.kiihdytä(-200)
print(f"Auton nopeus hätäjarrutuksen jälkeen: {volvo.nopeus} km/h")