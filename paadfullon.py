# This Python file uses the following encoding: utf-8

from setuptools import setup
from os import path

# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import and use built-in open()
from io import open as io_open
import re


summary = "Tool for automated PAADS"
project_homepage = "https://padupadoda.com"
here = path.abspath(path.dirname(__file__))


def readall(*args):
    with io_open(path.join(here, *args), encoding="utf-8") as fp:
        return fp.read()


with open("requirements.txt") as f:
    dependencies = f.read().splitlines()

documentation = readall("README.md")
metadata = dict(
    re.findall(r"""__([a-z]+)__ = "([^"]+)""", readall("padupy", "__init__.py"))
)
