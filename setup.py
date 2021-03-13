import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cep_to_coords",
    version="0.1.0",
    author="Gustavo Millen",
    author_email="millengustavo@gmail.com",
    description="Convert CEP (Brazilian zip code) to coordinates",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/millengustavo/cep_to_coords",
    packages=setuptools.find_packages("."),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
