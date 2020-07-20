import requests
import pycep_correios
from abc import ABC, abstractmethod


class CEPConverter(ABC):
    def __init__(self, cep):
        self.cep = cep

    @abstractmethod
    def factory_method(self):
        pass

    def convert_cep(self):
        strategy = self.factory_method()

        return strategy.convert()


class AddressConverter(CEPConverter):
    def factory_method(self):
        return AddressCoordinates(self.cep)


class Coordinates(ABC):
    def __init__(self, cep):
        self.cep = cep

    @abstractmethod
    def convert(self):
        pass


class AddressCoordinates(Coordinates):
    def fetch_address(self):
        try:
            search_result = pycep_correios.consultar_cep(self.cep)
            address = " ".join([search_result["end"], search_result["cidade"], "Brasil"])
            # Treating the case when Correios API return an empty json
            if address == " Brasil":
                address = "-"
        except:
            address = "-"

        return address

    def fetch_coordinates(self, address):
        try:
            if address == "-":
                print("Não foi possível converter, retornando NaNs...")
                return {"latitude": float("nan"), "longitude": float("nan")}

            r = requests.get("".join(["http://photon.komoot.de/api?q=", address, "&limit=1"]))

            result = r.json()
            # list with lon, lat
            coordinates = result["features"][0]["geometry"]["coordinates"]
            return {
                "latitude": coordinates[1],
                "longitude": coordinates[0]
            }
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    def convert(self):
        address = self.fetch_address()
        coordinates = self.fetch_coordinates(address)
        return coordinates


def cep_to_address_to_coords(cep: str) -> dict:
    converter = AddressConverter(cep)
    return converter.convert_cep()


if __name__ == "__main__":
    print(cep_to_address_to_coords("01310-200"))
    # {'latitude': -23.56150875, 'longitude': -46.65596048644724}