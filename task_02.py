#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lesson 08, Task 02 file"""


class Car(object):
    """A moving vehicle definition.

    Args:
        color (string): The color of the car. Defaults to ``'red'``.
        tires (list): A list of the car's tires.

    Attributes:
       color (string): The color of the car.
       tires (list): The car's tires.
    """

    def __init__(self, color='red', tires=None):
        self.color = color
        self.tires = tires
        if self.tires is None:
            self.tires = []
            for i in range(4):
                self.tires.append(Tire())


class Tire(object):
    """A round rubber thing.

    Args:
        miles (integer): The number of miles on the Tire. Defaults to 0.

    Attributes:
       miles (integer): The number of miles on the Tire.
    """

    __maximum_miles = 500

    def __init__(self, miles=0):
        self.miles = miles

    def add_miles(self, miles):
        """Increments the tire mileage by the specified miles.

        Args:
            miles (integer): The number of miles to add to the tire.
        """
        self.miles += miles
