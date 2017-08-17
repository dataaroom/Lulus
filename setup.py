# -*- coding: utf-8 -*-


import sys
from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tk8.6"

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('lulus.py', base=base)
]
icon = r'C:\Users\jiandong\Desktop\lulus_3.ico'

setup(name='unit converter',
      version='0.0.1',
      description='test version for Sarina',
      executables=executables
      )


