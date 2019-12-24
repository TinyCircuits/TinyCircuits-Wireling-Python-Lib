import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-TinyCircuits", 
    version="0.0.1",
    author="TinyCircuits",
    author_email="info@tinycircuits.com",
    description="Wireling Python library",
    long_description=long_description,,
    long_description_content_type="text/markdown",
    url="https://github.com/TinyCircuits/TinyCircuits-Wireling-Python-Lib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU LESSER GENERAL PUBLIC LICENSE",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)