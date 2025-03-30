import json
import requests

#lisää oma api-key
def main():
    key = str(open("/home/coy/.config/api/openweathermap", "r").read()).strip()

    city = input("Anna paikkakunta\n> ")
    for item in api_call(key, city):
        print(item)

def api_call(key, city):
    request = requests.get(f"https://api.openweathermap.org/data/2.5/weather?"
    f"lang=fi&q={city}&appid={key}&units=metric").json()

    return (request["weather"][0]["main"], request["main"]["temp"])

if __name__ == "__main__":
    main()