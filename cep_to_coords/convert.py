from .base import CEPConverter
from .strategies import CorreiosPhotonConverter


def cep_to_coords(cep: str, factory: CEPConverter = CorreiosPhotonConverter) -> dict:
    coordinates = factory()(cep)
    return coordinates
