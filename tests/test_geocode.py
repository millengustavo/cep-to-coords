import unittest
from src.geocode_python.geocode import cep_to_coords, address_from_cep, geocode


class TestGeocode(unittest.TestCase):

    def test_address_from_cep(self):
        d = {'01310-200': 'Avenida Paulista São Paulo Brasil',
             '22021001': 'Avenida Atlântica Rio de Janeiro Brasil',
             '': '-',
             '123456': '-'}

        self.assertEqual(
            d['01310-200'], address_from_cep('01310-200'), "Wrong result!")
        self.assertEqual(
            d['22021001'], address_from_cep('22021001'), "Wrong result!")
        self.assertEqual(
            d[''], address_from_cep(''), "Wrong result!")
        self.assertEqual(
            d['123456'], address_from_cep('123456'), "Wrong result!")

    def test_geocode(self):
        # Defining the values as tuples because lists are unhashable
        d = {'Avenida Paulista São Paulo Brasil': (-46.65596048644724, -23.56150875),
             'Avenida Atlântica Rio de Janeiro Brasil': (-43.189305, -22.984457),
             '-': (float('nan'), float('nan'))}

        self.assertEqual(
            d['Avenida Paulista São Paulo Brasil'], tuple(geocode('Avenida Paulista São Paulo Brasil')), "Wrong result!")
        self.assertEqual(
            d['Avenida Atlântica Rio de Janeiro Brasil'], tuple(geocode('Avenida Atlântica Rio de Janeiro Brasil')), "Wrong result!")
        self.assertEqual(
            str(d['-']), str(tuple(geocode('-'))), "Wrong result!")

    def test_cep_to_coords(self):
        # Defining the values as tuples because lists are unhashable
        d = {'01310-200': (-46.65596048644724, -23.56150875),
             '22021001': (-43.189305, -22.984457),
             '': (float('nan'), float('nan')),
             '123456': (float('nan'), float('nan'))}

        self.assertEqual(
            d['01310-200'], tuple(cep_to_coords('01310-200')), "Wrong result!")
        self.assertEqual(
            d['22021001'], tuple(cep_to_coords('22021001')), "Wrong result!")
        self.assertEqual(
            str(d['']), str(tuple(cep_to_coords(''))), "Wrong result!")
        self.assertEqual(
            str(d['123456']), str(tuple(cep_to_coords('123456'))), "Wrong result!")
