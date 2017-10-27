#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit Tests for the Conversions file"""

import unittest
import conversions

class TestKelvinValues(unittest.TestCase):
    testCtoKvalues = ((500.00, 773.15),
                      (400.00, 673.15),
                      (300.00, 573.15),
                      (200.00, 473.15),
                      (100.00, 373.15))

    def testConversionCelsiusToKelvin(self):
        for celsius, kelvin in self.testCtoKvalues:
            result = conversions.convertCelsiusToKelvin(celsius)
            self.assertEqual(kelvin, result)
            print 'Validating {} degrees Celsius to {} degrees Kelvin Conversion'.format(celsius, kelvin)

