# -*- coding: utf-8 -*-
"""
tomo_proj.py -- (back-)projections in tomography

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

from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from builtins import super
from future import standard_library
standard_library.install_aliases()

import numpy as np
from functools import partial
import gfunc
import fourier
from fourier import FourierProjector, FreqGeomGraphWarp
from operator import Operator, LinearOperator
from utility import euler_matrix, errfmt


class Projection(Operator):
    """Base class for tomographic projections.
    TODO: write some more.
    """
    
    def __init__(self, vol_geom, proj_geom, rotation=None):
        
        super().__init__(vol_geom, proj_geom)
        self.rotation = rotation

        
class BackProjection(Operator):
    """Base class for tomographic projections.
    TODO: write some more.
    """
    
    def __init__(self, proj_geom, vol_geom, rotation=None):
        
        super().__init__(proj_geom, vol_geom)
        self.rotation = rotation


class BornProjection(LinearOperator):
    
    def __init__(self, proj_grid, dist, wavenum, rotation=None, **kwargs):
        
        # The Born approximation graph is a half-sphere with radius k
        # centered at -k
        def halfsph(x, y, k):
            sq = np.sqrt(k**2 - x**2 - y**2)
            if np.any(np.isnan(sq)):
                raise ValueError(errfmt("""\
                Frequencies too large: k^2 - |freq|^2 has minimum {}.
                """.format(np.min((sq**2).real))))
            return k - sq

        halfsph_k = partial(halfsph, k=wavenum)

        if rotation is not None:
            rotation = np.asmatrix(rotation)
        else:
            phi = kwargs.get('phi', 0)
            theta = kwargs.get('theta', 0)
            psi = kwargs.get('psi', 0)
            if phi == 0 and theta == 0 and psi == 0:
                rotation = None
            else:
                rotation = euler_matrix(phi, theta, psi)
        

class BornProjector(FourierProjector):

    def __init__(self, vol_gfun, proj_grid, dist, wavenum, rotation=None,
                 **kwargs):


        # The grid warp is a rotation
        warp = lambda vec_arr, rot: vec_arr * rot
        rotate = partial(warp, rot=rotation) if rotation is not None else None

        # Feed the reciprocal projection grid into the frequency geometry
        proj_gr_recip = proj_grid.reciprocal()

        freq_geom = FreqGeomGraphWarp(proj_gr_recip.coord, halfsph_k, rotate)

        # post-processing is a multiplication by a (phase) factor
        def diffr_factor(x, y, k, d):
            sq = np.sqrt(k**2 - x**2 - y**2)
            # TODO: check factors and sign
            return -1j * np.sqrt(np.pi / 2) * np.exp(1j * d * sq) / sq

        diffr_factor_k_d = partial(diffr_factor, k=wavenum, d=dist)

        super().__init__(freq_geom, preproc=None)

        self.vol_gfun = vol_gfun
        self.proj_grid = proj_grid
        self.postproc = lambda x, y, f: f * diffr_factor_k_d(x, y)

    def __call__(self, backtrafo=True):
        proj_gfun = gfunc.asgfunc(self.proj_grid.reciprocal())
        proj_gfun.data = super().__call__(self.vol_gfun)
        proj_freqs = proj_gfun.coord.asarr()
        arglst = [col for col in proj_freqs.T] + [proj_gfun.data.flatten()]

        proj_gfun.data = self.postproc(*arglst)

        if backtrafo:
            return fourier.fourier_invtrafo_uni_uni(proj_gfun,
                                                    self.proj_grid.origin)
        else:
            return proj_gfun
