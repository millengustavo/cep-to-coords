import re
import string
import requests
import pycep_correios


class CEPConverter:
    def _clean_CEP(self, cep):
        # Regex to avoid CEPs with dash ('-')
        regex = re.compile("[%s]" % re.escape(string.punctuation))
        return regex.sub("", cep)

    def convert(self, cep):
        clean_cep = self._clean_CEP(cep)
        address_assembler = AddressAssembler(clean_cep)
        address = address_assembler.fetch_address()

        coordinates_assembler = CoordinatesAssembler(address)
        coordinates = coordinates_assembler.fetch_coordinates()

        return coordinates


class AddressAssembler:
    def __init__(self, cep):
        self.cep = cep

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
    

class CoordinatesAssembler:
    def __init__(self, address):
        self.address = address

    def fetch_coordinates(self):
        try:
            if self.address == "-":
                print("Não foi possível converter, retornando NaNs...")
                return {"latitude": float("nan"), "longitude": float("nan")}

            r = requests.get("".join(["http://photon.komoot.de/api?q=", self.address, "&limit=1"]))

            result = r.json()
            # list with lon, lat
            coordinates = result["features"][0]["geometry"]["coordinates"]
            return {
                "latitude": coordinates[1],
                "longitude": coordinates[0]
            }
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
