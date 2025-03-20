class Auto:
    def __init__(self, huippunopeus):
        self.nopeus = 0
        self.huippunopeus = huippunopeus

    def kiihdytä(self, kiihdytys):
        vauhti = self.nopeus + kiihdytys

        if vauhti > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif vauhti < 0:
            self.nopeus = 0
        else:
            self.nopeus = vauhti


volvo = Auto(142)

volvo.kiihdytä(30)
volvo.kiihdytä(70)
volvo.kiihdytä(50)

print(f"Auton nopeus kiihdytyksen jälkeen: {volvo.nopeus} km/h")

volvo.kiihdytä(-200)
print(f"Auton nopeus hätäjarrutuksen jälkeen: {volvo.nopeus} km/h")
