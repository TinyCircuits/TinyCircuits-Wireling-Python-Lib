import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-lennevia", # Replace with your own username
    version="0.0.1",
    author="TinyCircuits",
    author_email="info@tinycircuits.com",
    description="Wireling Python library",
    long_description=This library includes functions that make it easy to interface with Wireling products,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)