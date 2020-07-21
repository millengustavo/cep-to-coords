import unittest

from cep_to_coords.convert import cep_to_coords


class TestCepToCoords(unittest.TestCase):
    def test_cep_to_coords(self):
        # Defining the values as tuples because lists are unhashable
        d = {'01310-200': {"latitude": -23.56150875, "longitude": -46.65596048644724},
             '22021001': {"latitude": -22.9847059, "longitude": -43.1894432},
             '': {"latitude": float('nan'), "longitude": float('nan')},
             '123456': {"latitude": float('nan'), "longitude": float('nan')}}

        self.assertEqual(
            d['01310-200'], cep_to_coords('01310-200'), "Wrong result!")
        self.assertEqual(
            d['22021001'], cep_to_coords('22021001'), "Wrong result!")
        self.assertEqual(
            str(d['']), str(cep_to_coords('')), "Wrong result!")
        self.assertEqual(
            str(d['123456']), str(cep_to_coords('123456')), "Wrong result!")