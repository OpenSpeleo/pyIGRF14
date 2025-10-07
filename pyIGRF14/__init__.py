#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This is a package of IGRF-14 (International Geomagnetic Reference Field) about python version.
It don't need any Fortran compiler.
"""

__author__ = 'zzyztyy'
__version__ = "1.0.2"

from pyIGRF14.value import igrf_variation, igrf_value
from pyIGRF14 import loadCoeffs, calculate
