class Auto:
    pass

auto = Auto()
auto.rekkari = "ABC-123"
auto.huippu = 142
auto.nopeus = 0
auto.matka = 0


print (f"Auton ominaisuudet: "
       f"Rekisteri: {auto.rekkari:s}, Huippu nopeus: {auto.huippu:d}, Nopeus nyt: {auto.nopeus:d}, kuljettu matka: {auto.matka:d}.")