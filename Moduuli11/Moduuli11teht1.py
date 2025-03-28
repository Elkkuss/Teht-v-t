class Julkaisu:

    def __init__(self, nimi):
        self.nimi = nimi


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}, paatoimittaja: {self.paatoimittaja}")

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}, kirjoittaja: {self.kirjoittaja}, sivumaara: {self.sivumaara} sivua")


julkaisut = []
julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppa"))
julkaisut.append(Kirja("Hytti n:o 6", "Rosa Liksom", 200 ))

for t in julkaisut:
    t.tulosta_tiedot()


