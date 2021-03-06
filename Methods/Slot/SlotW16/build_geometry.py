"""
Created on 23 avr. 2018

@author: pierre_b
"""
# -*- coding: utf-8 -*-

from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Segment import Segment


def build_geometry(self):
    """Compute the curve (Line) needed to plot the Slot.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : SlotW16
        A SlotW16 object

    Returns
    -------
    curve_list: llist
        A list of 4 Segment and 5 Arc

    """

    Rbo = self.get_Rbo()

    [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9, Z10] = self._comp_point_coordinate()

    # Creation of curve
    curve_list = list()
    curve_list.append(Segment(Z1, Z2))
    curve_list.append(Arc1(Z2, Z3, -Rbo + self.H0))
    curve_list.append(Arc1(Z3, Z4, -self.R1))
    curve_list.append(Segment(Z4, Z5))
    curve_list.append(Arc1(Z5, Z6, Rbo - self.H0 - self.H2))
    curve_list.append(Segment(Z6, Z7))
    curve_list.append(Arc1(Z7, Z8, -self.R1))
    curve_list.append(Arc1(Z8, Z9, -Rbo + self.H0))
    curve_list.append(Segment(Z9, Z10))

    return curve_list
