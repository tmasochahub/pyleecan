# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW22.build_geometry_wind
SlotW22 build_geometry_wind method
@date Created on Mon Jan 12 16:20:43 2015
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import exp, linspace, meshgrid

from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine


def build_geometry_wind(self, Nrad, Ntan, is_simplified=False, alpha=0, delta=0):
    """Split the slot winding area in several zone

    Parameters
    ----------
    self : SlotW22
        A SlotW22 object
    Nrad : int
        Number of radial layer
    Ntan : int
        Number of tangentiel layer
    is_simplified : bool
        boolean to specify if coincident lines are considered as one or different lines (Default value = False)
    alpha : float
        Angle for rotation (Default value = 0) [rad]
    delta : Complex
        complex for translation (Default value = 0)

    Returns
    -------
    surf_list:
        List of surface delimiting the winding zone

    """

    if self.get_is_stator():  # check if the slot is on the stator
        st = "S"
    else:
        st = "R"

    Rbo = self.get_Rbo()

    # Polar Meshgrid
    if self.is_outwards():
        r = linspace(Rbo + self.H0, Rbo + self.H0 + self.H2, Nrad + 1)
    else:
        r = linspace(Rbo - self.H0, Rbo - self.H0 - self.H2, Nrad + 1)

    theta = linspace(-self.W2 / 2.0, self.W2 / 2.0, Ntan + 1)
    Z = meshgrid(r, theta)

    Z = Z[0] * exp(1j * Z[1])
    Z = Z.T
    if self.is_outwards():
        assert Z[0][0] == (Rbo + self.H0) * exp(-1j * self.W2 * 0.5)  # Z6
        assert Z[Nrad][0] == (Rbo + self.H0 + self.H2) * exp(-1j * self.W2 * 0.5)  # Z5
        assert Z[0][Ntan] == (Rbo + self.H0) * exp(1j * self.W2 * 0.5)  # Z3
        assert Z[Nrad][Ntan] == (Rbo + self.H0 + self.H2) * exp(
            1j * self.W2 * 0.5
        )  # Z4
    else:
        assert Z[0][0] == (Rbo - self.H0) * exp(-1j * self.W2 * 0.5)  # Z6
        assert Z[Nrad][0] == (Rbo - self.H0 - self.H2) * exp(-1j * self.W2 * 0.5)  # Z5
        assert Z[0][Ntan] == (Rbo - self.H0) * exp(1j * self.W2 * 0.5)  # Z3
        assert Z[Nrad][Ntan] == (Rbo - self.H0 - self.H2) * exp(
            1j * self.W2 * 0.5
        )  # Z4

    surf_list = list()
    for jj in range(Ntan):  # jj from 0 to Ntan-1
        for ii in range(Nrad):  # ii from 0 to Nrad-1
            Z1 = Z[ii][jj]
            Z2 = Z[ii][jj + 1]
            Z3 = Z[ii + 1][jj + 1]
            Z4 = Z[ii + 1][jj]
            point_ref = (
                Z[ii][jj] + Z[ii][jj + 1] + Z[ii + 1][jj + 1] + Z[ii + 1][jj]
            ) / 4  # the reference point of the surface
            if is_simplified:  # No doubling Line allowed
                curve_list = list()
                if ii == 0:
                    curve_list.append(Arc1(Z1, Z2, abs(Z1)))
                if jj != Ntan - 1:
                    curve_list.append(Segment(Z2, Z3))
                if ii != Nrad - 1:
                    curve_list.append(Arc1(Z3, Z4, -abs(Z3)))
                surface = SurfLine(
                    line_list=curve_list,
                    label="Wind" + st + "_R" + str(ii) + "_T" + str(jj) + "_S0",
                    point_ref=point_ref,
                )
                surf_list.append(surface)
            else:
                curve_list = list()
                curve_list.append(Arc1(Z1, Z2, abs(Z1)))
                curve_list.append(Segment(Z2, Z3))
                curve_list.append(Arc1(Z3, Z4, -abs(Z3)))
                curve_list.append(Segment(Z4, Z1))
                surface = SurfLine(
                    line_list=curve_list,
                    label="Wind" + st + "_R" + str(ii) + "_T" + str(jj) + "_S0",
                    point_ref=point_ref,
                )
                surf_list.append(surface)

    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)
    return surf_list
