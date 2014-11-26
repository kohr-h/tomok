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

import numpy as np

import curve as crv
from utility import errfmt


class LabComponent(object):

    def __init__(self, location, axes_map=None, **kwargs):

        if isinstance(location, crv.Curve):
            self._location = crv.curve(location, axes_map=axes_map,
                                       **kwargs)
        else:
            try:
                location = np.array(location)
                self._location = crv.FixedPoint(location, axes_map)
            except TypeError:
                raise TypeError(errfmt("""\
                `location` must either be array-like or a curve."""))

        self._cur_pos = self._location.startpos
        self._cur_coord_sys = self._location.start_coord_sys

    @property
    def location(self):
        return self._location

    @property
    def axes_map(self):
        return self.curve.axes_map

    @property
    def curve(self):
        return self._location

    @property
    def coord_sys(self):
        return self.curve.coord_sys

    @property
    def startpos(self):
        return self.curve.startpos

    @property
    def cur_pos(self):
        return self._cur_position

    @property
    def start_coord_sys(self):
        return self.curve.start_coord_sys

    @property
    def cur_coord_sys(self):
        return self._cur_coord_sys

    def moveto(self, param_val):
        self._cur_pos = self.curve.curve_fun(param_val)
        if self.axes_map is not None:
            self._cur_coord_sys = self.curve.axes_map(param_val)

    def reset(self):
        self._cur_pos = self.startpos
        if self.axes_map is not None:
            self._cur_coord_sys = self.start_coord_sys
