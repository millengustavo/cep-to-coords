import re
import string
import requests
import pycep_correios


def geocode(location,
            server="http://photon.komoot.de/"):
    """
    Returns latitude and longitude from Photon API using location
    OBS: The API returns other infos and can accept other inputs to narrow the search, 
    feel free to modify this function

    Parameters
    ----------
    location : str
        String with relevant location identifiers (address, city, country)

    Returns
    -------
    coords : list 
        Geographic coordinates list composed by [lon, lat] floats
    """

    try:
        if location == '-':
            return [float('nan'), float('nan')]
        r = requests.get(server + 'api?q=' + location + "&limit=1")
        print('Requesting coordinates from {}'.format(location))
        result = r.json()
        coords = result['features'][0]['geometry']['coordinates']
        return coords
    except Exception as e:
        print(e)


def address_from_cep(cep, country='Brasil'):
    """
    Get address and city from pycep_correios using zipcode (CEP)

    Parameters
    ----------
    cep : str
        Brazilian zipcode (CEP) - only numbers

    Returns
    -------
    address : str 
        Concatenated string with address, city and country
    """
    try:
        search = pycep_correios.consultar_cep(cep)
        address = search['end'] + ' ' + search['cidade'] + ' ' + country
        # Treating the case when Correios API return an empty json
        if address == '  ' + country:
            address = '-'
    except:
        address = '-'
        # print(e)

    return address


def cep_to_coords(cep):
    """
    Returns lat and long from CEP (brazilian zipcode)

    Parameters
    ----------
    cep : str
        String with Brazilian zipcode (CEP). ex:
        '01310-200', '22021001', '20271-130'

    Returns
    -------
    coords : list 
        Geographic coordinates list composed by [lat, lon] floats
    """
    # Regex to avoid CEPs with dash ('-')
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    try:
        cep = regex.sub('', cep)
        coords = geocode(address_from_cep(cep))
    except Exception as e:
        coords = [float('nan'), float('nan')]
        print(e)

    return coords


# if __name__ == "__main__":
#     test_cep = '20271-130'
#     coords = cep_to_coords(test_cep)
#     print(coords)
