#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lesson 08, Task 04"""

import task_02


class Tigerpaw(task_02.Tire):
    """A Tigerpaw Tire.

    Args:
        miles (integer): The number of miles on the Tire. Defaults to 0.

    Attributes:
       miles (integer): The number of miles on the Tire.
    """


    def __init__(self):
        __maximum_mileage = 750
