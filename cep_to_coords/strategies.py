import os
import requests
import pycep_correios
from .base import CEPConverter, Coordinates


class CorreiosPhotonConverter(CEPConverter):
    def __call__(self, cep):
        return CorreiosPhotonCoordinates(cep)()


class CEPAbertoConverter(CEPConverter):
    def __call__(self, cep):
        return CEPAbertoCoordinates(cep)()


class CorreiosPhotonCoordinates(Coordinates):
    def fetch_address(self):
        try:
            search_result = pycep_correios.consultar_cep(self.clean_cep)
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

    def __call__(self):
        address = self.fetch_address()
        coordinates = self.fetch_coordinates(address)
        return coordinates


class CEPAbertoCoordinates(Coordinates):
    def fetch_coordinates(self):
        try:
            url = f"https://www.cepaberto.com/api/v3/cep?cep={self.clean_cep}"
            # Sign up for your free token on: https://cepaberto.com/
            # export CEP_ABERTO_TOKEN='your-token'
            headers = {'Authorization': f'Token token={os.getenv("CEP_ABERTO_TOKEN")}'}
            response = requests.get(url, headers=headers)
            json_response = response.json()
            return {
                "latitude": float(json_response["latitude"]),
                "longitude": float(json_response["longitude"]),
            } 
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    def __call__(self):
        coordinates = self.fetch_coordinates()
        return coordinates


def cep_to_coords(factory: CEPConverter, cep: str) -> dict:
    coordinates = factory()(cep)
    return coordinates


if __name__ == "__main__":
    print(cep_to_coords(CorreiosPhotonConverter, "01310-200"))
    # OR
    # print(CorreiosPhotonConverter()("01310-200"))
    # OR
    # export CEP_ABERTO_TOKEN='your-token'
    # print(cep_to_coords(CEPAbertoConverter, "01310-200"))
    # {'latitude': -23.56150875, 'longitude': -46.65596048644724}