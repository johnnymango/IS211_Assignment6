#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Assignment 6 - Unit Tests for the Conversions file"""

import unittest
import conversions
import conversions_refactored


#Class creates a conversion table that is called by all of the test cases to check the conversion.
class conversionInfo():
    conversiontable = (
                        (500.00, 932.00, 773.15),
                        (400.00, 752.00, 673.15),
                        (300.00, 572.00, 573.15),
                        (200.00, 392.00, 473.15),
                        (100.00, 212.00, 373.15),
                        (0.00, 32.00, 273.15),
                        (-100.00, -148.00, 173.15)
                       )

#Individual conversion test cases are checked against the conversion table.
class testTemperatureCases(unittest.TestCase):

    #Function tests the Celsius to Kelvin Conversion
    def testConversionCelsiusToKelvin(self):
        for celsius, fahrenheit, kelvin in conversionInfo.conversiontable:
            print 'Validating {} degrees Celsius to {} degrees Kelvin Conversion'.format(celsius, kelvin)
            result = conversions.convertCelsiusToKelvin(celsius)
            self.assertEqual(kelvin, round(result, 2))

    #Function tests the Celsius to Fahrenheit conversion
    def testConversionCelsiusToFahrenheit(self):
         for celsius, fahrenheit, kelvin in conversionInfo.conversiontable:
             print 'Validating {} degrees Celsius to {} degrees Fahrenheit Conversion'.format(celsius, fahrenheit)
             result = conversions.convertCelsiusToFahrenheit(celsius)
             self.assertEqual(fahrenheit, round(result, 2))

    #Function tests the Fahrenheit to Celsius conversion
    def testConversionFahrenheitToCelsius(self):
         for celsius, fahrenheit, kelvin in conversionInfo.conversiontable:
             print 'Validating {} degrees Fahrenheit to {} degrees Celsius Conversion'.format(fahrenheit, celsius)
             result = conversions.convertFahrenheitToCelsius(fahrenheit)
             self.assertEqual(celsius, round(result, 2))


    #Function tests the Fahrenheit to Kelvin conversion
    def testConversionFahrenheitToKelvin(self):
        for celsius, fahrenheit, kelvin in conversionInfo.conversiontable:
            print 'Validating {} degrees Fahrenheit converts to {} degrees Kelvin'.format(fahrenheit, kelvin)
            result = conversions.convertFahrenheitToKelvin(fahrenheit)
            self.assertEqual(kelvin, round(result, 2))

    #Function tests the Kelvin to Celsius conversion
    def testConversionKelvinToCelsius(self):
        for celsius, fahrenheit, kelvin in conversionInfo.conversiontable:
            print 'Validating {} degrees Kelvin converts to {} degrees Celsius'.format(kelvin, celsius)
            result = conversions.convertKelvinToCelsius(kelvin)
            self.assertEqual(celsius, round(result, 2))


    #Function tests the Kelvin to Fahrenheit conversion
    def testConversionKelvinToFahrenheit(self):
        for celsius, fahrenheit, kelvin in conversionInfo.conversiontable:
            print 'Validating {} degrees Kelvin converts to {} degrees Fahrenheit'.format(kelvin, fahrenheit)
            result = conversions.convertKelvintoFahrenheit(kelvin)
            self.assertEqual(fahrenheit, round(result, 2))


#Class creates testcases for all conversion types for the refactored code
class GeneralConversionInfo():

    testcases = (
                ("CElsius", "KELVIN", 410.00, 683.150),
                ("kelvin", "Celsius", 573.15, 300.00),
                ("kelvin", "Celsius", 683.15, 410.00),
                ("Kelvin", "celsius", 393.15, 120.00),
                ("fahrenheit", "kelvin", 572.00, 573.15),
                ("Fahrenheit", "Kelvin", 770.00, 683.15),
                ('miles', 'yards', 1.00, 1760.00),
                ('meters', 'yards', 50.00, 54.68),
                ('miles', 'meters', 5.00, 8046.72),
                ('meters', 'miles', 5000.00, 3.11),
                ('yards', 'miles',  8800.00, 5.00),
                ('yards', 'meters', 450.00, 411.48),
                ('yards', 'yards', 10, 10),
                ('celsius', 'celsius', 100, 100)
                )

#Class calls on the test cases to validate refactored code.
class refactoredTestCases(unittest.TestCase):

    def testRefactoredTempCases(self):
        for fromUnit, toUnit, value, conversion in GeneralConversionInfo.testcases:
            result = conversions_refactored.conversioncalcs(fromUnit, toUnit, value)
            self.assertEqual(conversion, round(result, 2))


if __name__ == '__main__':
    unittest.main()