#!/usr/bin/env python

"""
Time and units conversion functions
"""

from datetime import datetime

__KELVIN_OFFSET__ = 273.15
__FAHRENHEIT_OFFSET = 32.0
__FAHRENHEIT_DEGREE_SCALE = 1.8

def unix_to_ISO8601(unixtime):
    """
    Converts a int/long UNIX time to the correspondant ISO 8601 string
    The result is in the format: [YYYY]-[MM]-[DD] [HH]:[MM]:[SS]+00
    """
    if type(unixtime) is long or type(unixtime) is int: 
        return datetime.utcfromtimestamp(unixtime).strftime('%Y-%m-%d %H:%M:%S+00')
    else:
        raise ValueError(__name__+": unable to convert to ISO 8601 string")

def kelvin_to_celsius(kelvintemp):
    """
    Converts a float temperature from Kelvin degrees to Celsius degrees
    """
    celsiustemp = kelvintemp - __KELVIN_OFFSET__
    return float("{0:.2f}".format(celsiustemp))

def kelvin_to_fahrenheit(kelvintemp):
    """
    Converts a float temperature from Kelvin degrees to Fahrenheit degrees
    """
    fahrenheittemp = (kelvintemp - __KELVIN_OFFSET__)*__FAHRENHEIT_DEGREE_SCALE + __FAHRENHEIT_OFFSET
    return float("{0:.2f}".format(fahrenheittemp))