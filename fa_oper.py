# -*- coding: utf-8 -*-
"""
operator.py -- functional analytic operators

Copyright 2014 Holger Kohr

This file is part of tomok.

tomok is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

tomok is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with tomok.  If not, see <http://www.gnu.org/licenses/>.
"""

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from builtins import object

from copy import deepcopy


class Operator(object):
    """Basic class for a functional analytic operator.
    TODO: write some more
    """
    # TODO: define next() instead of making a list?
    def __init__(self, map_, domain_in=None, domain_out=None, **kwargs):

        self._map = map_
        self._domain_in = domain_in
        self._domain_out = domain_out
        self._operator_steps = [self]

    @property
    def map_(self):
        if self._operator_steps == [self]:
            return self._map
        else:
            return self.__call__

    @property
    def domain_in(self):
        return self._operator_steps[-1]._domain_in

    @property
    def domain_out(self):
        return self._operator_steps[0]._domain_out

    @property
    def operator_steps(self):
        return self._operator_steps

    def __call__(self, function_in):
        interm_func = function_in
        for op in reversed(self.operator_steps):
            if op == self:
                interm_func = op._map(interm_func)
                return interm_func
            else:
                interm_func = op(interm_func)

    def __mul__(self, other):
        if isinstance(other, Operator):  # return operator product
            new_op = self.copy()
            new_op.__imul__(other)
            return new_op
        else:  # try to evaluate
            return self.__call__(other)

    def __imul__(self, other):
        if not isinstance(other, Operator):
            raise TypeError("`other` must be of `Operator` type")
        self.operator_steps.append(other.copy())

    def copy(self):
        return deepcopy(self)


class LinearOperator(Operator):
    """Basic class for a functional analytic linear operator.
    TODO: write some more
    """
    pass
