# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 00:12:06 2014

@author: hkohr
"""
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from builtins import object


class Operator(object):
    """Basic class for a functional analytic operator.
    TODO: write some more
    """

    def __init__(self, geom_in, geom_out, **kwargs):

        self._geom_in = geom_in
        self._geom_out = geom_out

    def __call__(self, fun_in, fun_out=None):
        raise NotImplementedError


class LinearOperator(Operator):
    """Basic class for a functional analytic linear operator.
    TODO: write some more
    """
    pass
