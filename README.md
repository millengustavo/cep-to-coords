# Python package to get Coordinates based on the address

# How to use:
1. Install from source
```bash
git clone https://github.com/millengustavo/geocode_python.git
cd geocode_python
git checkout master
pip install -e .
```

2. Convert CEP to longitude and latitude:
```python
from geocode_python.geocode import cep_to_coords

lon, lat = cep_to_coords('22070-900')

>>> print('Latitude: {}, Longitude: {}'.format(lat, lon))
Latitude: -22.9864082, Longitude: -43.189592
```


# Basic testing
```bash
python -m unittest discover
```