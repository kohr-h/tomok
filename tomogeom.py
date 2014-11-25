# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 17:35:13 2014

@author: hkohr
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
