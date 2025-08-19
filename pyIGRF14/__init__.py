#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'zzyztyy'

"""
This is a package of IGRF-14 (International Geomagnetic Reference Field) about python version.
It don't need any Fortran compiler.
"""

from pyIGRF14.value import igrf_variation, igrf_value
from pyIGRF14 import loadCoeffs, calculate
