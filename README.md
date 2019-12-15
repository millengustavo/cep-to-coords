# Pacote Python para converter CEP em latitude e longitude

https://cep-to-coords.readthedocs.io/en/latest/

# Como usar:
1. Instale:
```bash
git clone https://github.com/millengustavo/cep_to_coords.git
cd cep_to_coords
git checkout master
pip install -e .
```

2. Converta um CEP para latitude e longitude:
```python
from cep_to_coords.geocode import cep_to_coords

lat, lon = cep_to_coords('22070-900')

>>> print('Latitude: {}, Longitude: {}'.format(lat, lon))
Latitude: -22.9864082, Longitude: -43.189592
```


# Testando
```bash
python -m unittest discover
```

# Documentação

https://cep-to-coords.readthedocs.io/en/latest/