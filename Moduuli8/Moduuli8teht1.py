def main():
    import mysql.connector
    yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='elkku',
        password='salis',
        autocommit=True,
        collation='utf8mb3_general_ci'
    )

    print("Anna ICAO-koodi")
    icao = input("> ")
    print(hae_nimi(yhteys, icao))


def hae_nimi(yhteys, koodi):
    sql = f"SELECT name FROM airport where ident='{koodi}'"
    merkki = yhteys.cursor()
    merkki.execute(sql)
    tulos = merkki.fetchone()
    if merkki.rowcount > 0:
        return tulos[0]


main()