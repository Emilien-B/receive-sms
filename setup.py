from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.3'
DESCRIPTION = 'Receive SMS'
LONG_DESCRIPTION = 'receive_sms is a library which allows to receive SMS in python free and unlimited.'

# Setting up
setup(
    name="receive-sms",
    version=VERSION,
    author="EmilienB",
    author_email="emilien.barde@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/Emilien-B/receive-sms",
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python','python3', 'sms', 'receive','message','free','unlimited','scraping'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)