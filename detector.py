# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 14:26:14 2014

@author: hkohr
"""
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import super
from future import standard_library
standard_library.install_aliases()

from labcomp import LabComponent


class Detector(LabComponent):

    def __init__(self, support, location, axes_map=None, **kwargs):

        self._support = support
        super().__init__(location, axes_map, **kwargs)

    @property
    def support(self):
        return self._support


class FlatDetectorArray(Detector):

    def __init__(self, grid, location, axes_map=None, **kwargs):
        super().__init__(grid, location, axes_map, **kwargs)

    @property
    def grid(self):
        return self.support


class SphericalDetectorArray(Detector):

    def __init__(self, grid, location, axes_map=None, **kwargs):
        super().__init__(grid, location, axes_map, **kwargs)

    @property
    def grid(self):
        return self.support


class PointDetectors(Detector):

    # TODO: implement point colletion type support
    def __init__(self, points, axes_map=None, **kwargs):
        super().__init__(points, None, axes_map, **kwargs)

    @property
    def points(self):
        return self.support
