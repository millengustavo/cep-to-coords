===============
Getting started
===============

Installation
------------

You can install this package from source::

    # clone the repository
    $ git clone https://github.com/millengustavo/cep_to_coords.git
    
    # open the folder
    $ cd cep_to_coords
    
    # install the dependencies
    $ pip install -e .

Usage
-----

Convert a CEP to latitude and longitude::

    from cep_to_coords.geocode import cep_to_coords

    lat, lon = cep_to_coords('22070-900')

    >>> print('Latitude: {}, Longitude: {}'.format(lat, lon))
    Latitude: -22.9864082, Longitude: -43.189592



Testing
-------

Navigate to the root folder and run ::

    $ python -m unittest discover
