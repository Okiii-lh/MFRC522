import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mfrc522",
    version="0.0.1",
    author="Tech_lh",
    author_email="liuh131@163.com",
    description="A library to integrate the MFRC522 RFID readers with the Raspberry Pi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pimylifeup/MFRC522-python",
    packages=setuptools.find_packages(),
    install_requires=[
        'RPi.GPIO',
        'spidev'
        ],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: POSIX :: Linux",
        'Topic :: System :: Hardware',
    ],
)