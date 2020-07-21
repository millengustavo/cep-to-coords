import re
import string
from abc import ABC, abstractmethod


class CEPConverter(ABC):
    @abstractmethod
    def __call__(self, cep):
        pass


class Coordinates(ABC):
    def __init__(self, cep):
        self.cep = cep
        self.clean_cep = self._clean_CEP()

    def _clean_CEP(self):
        # Regex to avoid CEPs with dash ('-')
        regex = re.compile("[%s]" % re.escape(string.punctuation))
        return regex.sub("", self.cep)

    @abstractmethod
    def __call__(self):
        pass