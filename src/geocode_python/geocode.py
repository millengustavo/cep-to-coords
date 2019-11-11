import requests
import pycep_correios


def geocode(location,
            server="http://photon.komoot.de/"):

    try:
        r = requests.get(server + 'api?q=' + location + "&limit=1")
        print('Requesting coordinates from {}'.format(location))
        result = r.json()
        coords = result['features'][0]['geometry']['coordinates']
        return coords
    except Exception as e:
        print(e)


def address_from_cep(cep):
    try:
        search = pycep_correios.consultar_cep(cep)
        address = search['end'] + ' ' + search['cidade'] + ' Brasil'
    except Exception as e:
        address = '-'
        print(e)

    return address


if __name__ == "__main__":
    coords = geocode(address_from_cep('01310200'))
    print(coords)
