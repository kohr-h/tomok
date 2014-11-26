# -*- coding: utf-8 -*-
"""
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
