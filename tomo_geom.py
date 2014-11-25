# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 14:26:28 2014

@author: hkohr
"""

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from builtins import object


class Geometry(object):

    def __init__(self, source, sample, detector, *args, **kwargs):

        self._source = source
        self._sample = sample
        self._detector = detector

    @property
    def source(self):
        return self._source

    @property
    def sample(self):
        return self._sample

    @property
    def detector(self):
        return self._detector

    # TODO: add more features
