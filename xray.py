# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21 23:39:58 2014

@author: hkohr
"""
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()

import numpy as np
from math import pi

import ugrid as ug
import curve as crv
import source as src
import sample as spl
import detector as det
import tomo_geom as tgeo
from utility import InputValidationError


def xray_ct_parallel_geom_3d(spl_grid, det_grid, axis, angles=None,
                             rotating_sample=True, **kwargs):

    spl_grid = ug.ugrid(spl_grid)
    det_grid = ug.ugrid(det_grid)
    if not spl_grid.dim == 3:
        raise InputValidationError('spl_grid.dim', 3)
    if not det_grid.dim == 2:
        raise InputValidationError('det_grid.dim', 2)

    if angles is not None:
        angles = np.array(angles)

    init_rotation = kwargs.get('init_rotation', None)

    if rotating_sample:
        # TODO: make axis between source and detector flexible; now: -x axis
        direction = (1, 0, 0)
        src_loc = (-1, 0, 0)
        source = src.ParallelRaySource(direction, src_loc)
        sample = spl.RotatingGridSample(spl_grid, axis, init_rotation,
                                        angles=angles, **kwargs)
        det_loc = (-1, 0, 0)
        detector = det.FlatDetectorArray(det_grid, det_loc)
    else:
        src_circle = crv.Circle3D(1., axis, angles=angles, axes_map='tripod')
        source = src.ParallelRaySource(curve=src_circle)

        sample = spl.FixedSample(spl_grid)

        det_circle = crv.Circle3D(1., axis, angle_shift=pi, angles=angles,
                                  axes_map='tripod')
        detector = det.FlatDetectorArray(det_grid, det_circle)
    return tgeo.Geometry(source, sample, detector)
