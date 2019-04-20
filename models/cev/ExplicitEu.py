#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 22:30:45 2017

@author: Quintus
"""

import numpy as np

from .FiniteDifferences import FiniteDifferences

class ExplicitEu(FiniteDifferences):
        
    def _setup_boundary_conditions_(self):
        # terminal condition
        if self.is_call:
            self.grid[:, -1] = np.maximum(self.SValues - self.K, 0)
        else:
            self.grid[:, -1] = np.maximum(self.K - self.SValues, 0)
            
        # side boundary conditions
        self.coeffs[0,   0] += 2*self.alpha[0]
        self.coeffs[0,   1] -= self.alpha[0]
        self.coeffs[-1, -1] += 2*self.gamma[-1]
        self.coeffs[-1, -2] -= self.gamma[-1]
        
    def _traverse_grid_(self):
        for j in reversed(self.jValues):
            self.grid[1:-1, j] = np.dot(self.coeffs, self.grid[1:-1, j+1])
            self.grid[0, j] = 2 * self.grid[1, j] - self.grid[2, j]
            self.grid[-1, j] = 2 * self.grid[-2, j] - self.grid[-3, j]

    