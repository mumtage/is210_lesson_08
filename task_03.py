#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lesson 08, Task 03"""

import time


class Snapshot(object):
    """A moment in time.

    Attributes:
        created = Unix Timestamp of when Snapshot was created.

    """


    def __init__(self):
        self.created = time.time()
