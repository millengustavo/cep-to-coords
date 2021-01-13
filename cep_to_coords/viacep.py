import json
import requests


URL_GET_ADDRESS_FROM_CEP = "http://www.viacep.com.br/ws/{}/json"


class BaseException(Exception):
    """ base exception"""

    def __init__(self, message=""):
        super(BaseException, self).__init__(message)
        self.message = message

    def __repr__(self):
        return "%s(%r)" % (self.__class__.__name__, self.message)


def get_address_from_cep(cep):
    """ Source: https://github.com/mstuttgart/pycep-correios/blob/develop/pycep_correios/client.py """
    try:
        response = requests.get(URL_GET_ADDRESS_FROM_CEP.format(cep))

        if response.status_code == 200:
            address = json.loads(response.text)

            if address.get("erro"):
                raise BaseException(message="Other error")

            return {
                "bairro": address.get("bairro", ""),
                "cep": address.get("cep", ""),
                "cidade": address.get("localidade", ""),
                "logradouro": address.get("logradouro", ""),
                "uf": address.get("uf", ""),
                "complemento": address.get("complemento", ""),
            }

        elif response.status_code == 400:
            raise BaseException(message="Invalid CEP: %s" % cep)  # noqa
        else:
            raise BaseException(message="Other error")

    except requests.exceptions.RequestException as e:
        raise BaseException(message=e)
