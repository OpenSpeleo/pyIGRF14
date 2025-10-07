#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This is a package of IGRF-14 (International Geomagnetic Reference Field) about python version.
It don't need any Fortran compiler.
"""

__author__ = "zzyztyy"
__version__ = "1.0.3"

from pyIGRF14 import calculate, loadCoeffs  # noqa: F401
from pyIGRF14.value import igrf_value, igrf_variation  # noqa: F401
