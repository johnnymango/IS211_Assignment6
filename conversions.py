#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Temperature Conversions"""


#Function converts C to K
def convertCelsiusToKelvin(celsius):
     kelvin = celsius + 273.15
     return float(kelvin)

#Function converts C to F
def convertCelsiusToFahrenheit(celsius):
     fahrenheit = (celsius * 9) / 5 + 32
     return float(fahrenheit)

#Function converts F to C
def convertFahrenheitToCelsius(fahrenheit):
     celsius = ((fahrenheit - 32) * 5) / 9
     return float(celsius)

#Function converts F to K
def convertFahrenheitToKelvin(fahrenheit):
     kelvin = (fahrenheit + 459.67) * 5/9
     return float(kelvin)

#Function converts K to C
def convertKelvinToCelsius(kelvin):
     celsius = kelvin - 273.15
     return float(celsius)

#Function converts K to F
def convertKelvintoFahrenheit(kelvin):
     fahrenheit = (kelvin * 9/5) - 459.67
     return float(fahrenheit)


