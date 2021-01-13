import os
import requests

from .viacep import get_address_from_cep
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
            search_result = get_address_from_cep(self.clean_cep)
            address = " ".join(
                [
                    search_result["logradouro"],
                    search_result["bairro"],
                    search_result["cidade"],
                    search_result["uf"],
                    "Brasil",
                ]
            )
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

            r = requests.get(
                "".join(["http://photon.komoot.de/api?q=", address, "&limit=1"])
            )

            result = r.json()
            # list with lon, lat
            coordinates = result["features"][0]["geometry"]["coordinates"]
            return {"latitude": coordinates[1], "longitude": coordinates[0]}
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
            headers = {"Authorization": f'Token token={os.getenv("CEP_ABERTO_TOKEN")}'}
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
