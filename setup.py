import re
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand

# Parse the version from the file.
verstrline = open('vimv.py', "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in vimv.py")


setup(
    version=verstr,
    entry_points={'console_scripts': 'vimv=vimv:main'},
)
