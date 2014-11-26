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

from ugrid import Ugrid
from astra import create_proj_geom, create_vol_geom


# TODO: check axes order, maybe use option 'ij' or 'xy' like in meshgrid
# TODO: include scaling of volume
def volgeom_from_ugrid2(ugrid2):
    return create_vol_geom(ugrid2.shape[1], ugrid2.shape[0])


def volgeom_from_ugrid3(ugrid3):
    return create_vol_geom(ugrid3.shape[1], ugrid3.shape[2], ugrid3.shape[0])


def ugrid3_from_volgeom(volgeom):
    return Ugrid3((volgeom['GridSliceCount'], volgeom['GridRowCount'],
                   volgeom['GridColCount']))


def projgeom_from_ugrid2_and_angles(ugrid2, angles):
    projgeo = create_proj_geom('parallel3d',
                               ugrid2.spacing[0], ugrid2.spacing[1],
                               ugrid2.shape[1], ugrid2.shape[0],
                               angles)
    return projgeo


def ugrid2_from_projgeom(projgeom):
    ugrid2 = Ugrid2((projgeom['DetectorColCount'],
                     projgeom['DetectorRowCount']),
                    (projgeom['DetectorSpacingX'],
                     projgeom['DetectorSpacingY']))
    return ugrid2
