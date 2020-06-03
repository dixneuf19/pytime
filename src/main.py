import requests

def main():
    r = requests.get("http://worldtimeapi.org/api/timezone/Europe/Paris")
    datetime = r.json()["datetime"]
    print(datetime)

if __name__ == "__main__":
    main()
