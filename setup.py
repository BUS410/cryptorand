import setuptools

with open("README.txt", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cryptorand", # Replace with your own username
    version="0.1.0",
    author="BUS410",
    description="A small module for crytp",
    long_description=long_description,
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)