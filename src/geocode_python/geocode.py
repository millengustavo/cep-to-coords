import requests
import pandas as pd


def geocode(location,
            server="http://photon.komoot.de/"):

    for loc in location:
        try:
            r = requests.get(server + 'api?q=' + loc)
            print(r.json())
        except Exception as e:
            print(e)


if __name__ == "__main__":
    geocode(['SaoPaulo'])
