#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Assignment 6 - Refactored Conversions Code"""

class ConversionNotPossible():
    pass


def conversioncalcs(fromUnit, toUnit, value):

    #Calculates valid temperature conversions
    if fromUnit.lower() == 'celsius' and toUnit.lower() == 'kelvin':
        kelvin = value + 273.15
        print '{} degrees Celsius is equal to {} degrees Kelvin'.format(value, kelvin)
        return kelvin
    elif fromUnit.lower() == 'celsius' and toUnit.lower() == 'fahrenheit':
        fahrenheit = (value * 9) / 5 + 32
        print '{} degrees Celsius is equal to {} degrees Fahrenheit'.format(value, fahrenheit)
        return fahrenheit
    elif fromUnit.lower() == 'fahrenheit' and toUnit.lower() == 'celsius':
        celsius = ((value - 32) * 5) / 9
        print '{} degrees Fahrenheir is equal to {} degrees Celsius'.format(value, celsius)
        return celsius
    elif fromUnit.lower() == 'fahrenheit' and toUnit.lower() == 'kelvin':
        kelvin = (value + 459.67) * 5 / 9
        print '{} degrees Fahrenheit is equal to {} degrees Kelvin'.format(value, kelvin)
        return kelvin
    elif fromUnit.lower() == 'kelvin' and toUnit.lower() == 'celsius':
        celsius = value - 273.15
        print '{} degrees Kelvin is equal to {} degrees Celsius'.format(value, celsius)
        return celsius
    elif fromUnit.lower() == 'kelvin' and toUnit.lower() == 'fahrenheit':
        fahrenheit = (value * 9 / 5) - 459.67
        print '{} degrees Kelvin is equal to {} degrees Fahrenheit'.format(value, fahrenheit)
        return fahrenheit

    #Calculate valid distance conversions
    elif fromUnit.lower() == 'miles' and toUnit.lower()== 'yards':
        yards = value * 1760
        print '{} miles is equal to {} yards.'.format(value, yards)
        return yards
    elif fromUnit.lower() == 'miles' and toUnit.lower()== 'meters':
        meters = value * 1609.344
        print '{} miles is equal to {} meters.'.format(value, meters)
        return meters
    elif fromUnit.lower() == 'meters' and toUnit.lower()== 'miles':
        miles = value / 1609.344
        print '{} meters is equal to {} miles.'.format(value, miles)
        return miles
    elif fromUnit.lower() == 'meters' and toUnit.lower()== 'yards':
        yards = value / .9144
        print '{} meters is equal to {} yards.'.format(value, yards)
        return yards
    elif fromUnit.lower() == 'yards' and toUnit.lower()== 'miles':
        miles = value / 1760
        print '{} yards is equal to {} miles.'.format(value, miles)
        return miles
    elif fromUnit.lower() == 'yards' and toUnit.lower()== 'meters':
        yards = value * .9144
        print '{} miles is equal to {} yards.'.format(value, yards)
        return yards


    else:
       raise ConversionNotPossible('This is not a Valid Conversion!')






