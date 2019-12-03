import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="geocode_python-millengustavo",
    version="0.0.1",
    author="Gustavo Millen",
    author_email="millengustavo@gmail.com",
    description="Convert CEP (Brazilian zip code) to coordinates",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/millengustavo/geocode_python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
