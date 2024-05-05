#!/home/plo/ab/renpy/lib/py3-linux-x86_64/python

# Builds a distribution of Ren'Py.
from __future__ import division, absolute_import, with_statement, print_function, unicode_literals

import future.standard_library
import future.utils
PY2 = future.utils.PY2

import sys
import os
import compileall
import shutil
import subprocess
import argparse
import time
import collections

try:
    from importlib import reload
except ImportError:
    pass


ROOT = os.path.dirname(os.path.abspath(__file__))


def zip_rapt_symbols(destination):
    """
    Zips up the rapt symbols.
    """

    import zipfile

    if PY2:
        zf = zipfile.ZipFile(destination + "/android-native-symbols.zip", "w", zipfile.ZIP_DEFLATED)
    else:
        zf = zipfile.ZipFile(destination + "/android-native-symbols.zip", "w", zipfile.ZIP_DEFLATED, compresslevel=3)

    for dn, dirs, files in os.walk("rapt/symbols"):
        for fn in dirs + files:
            fn = os.path.join(dn, fn)
            arcname = os.path.relpath(fn, "rapt/symbols")
            zf.write(fn, arcname)

    zf.close()
