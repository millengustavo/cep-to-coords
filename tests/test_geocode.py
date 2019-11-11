import unittest
from src.geocode_python.geocode import cep_to_coords


class TestCEPtoCoords(unittest.TestCase):

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
