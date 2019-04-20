#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

class FiniteDifferences:
    """ Shared attributes and functions of FD """

    def __init__(self, K, r, q, T, alpha_cev, beta_cev, Smax, M, N, is_call=True):
        self.K = K
        self.r = r
        self.q = q
        self.T = T
        self.alpha_cev = alpha_cev
        self.beta_cev = beta_cev
        self.is_call = is_call

        self.Smax = Smax
        self.M, self.N = int(M), int(N)  # Ensure M&N are integers

        self.dS = Smax / float(self.M)
        self.dt = T / float(self.N)
        self.iValues = np.arange(1, self.M)
        self.jValues = np.arange(self.N)
        self.grid = np.zeros(shape=(self.M+1, self.N+1)) # grid is M+1 by N+1
        self.SValues = np.linspace(0, Smax, self.M+1)
        self.TValues = np.linspace(0, T, self.N+1)

        self.traversed = False

    def _setup_boundary_conditions_(self):
        pass

    def _setup_coefficients_(self):
        pass

    def _traverse_grid_(self):
        """  Iterate the grid backwards in time """
        pass

    def _interpolate_(self, S0):
        """
        Use piecewise linear interpolation on the initial
        grid column to get the closest price at S0.
        """
        return np.interp(S0,
                         self.SValues,
                         self.grid[:, 0])

    def price(self, S0):
        if not self.traversed:
            self._setup_coefficients_()
            self._setup_boundary_conditions_()
            self._traverse_grid_()
            self.traversed = True
        return self._interpolate_(S0)