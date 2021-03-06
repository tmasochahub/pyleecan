# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotMFlat.comp_W0m
SlotMFlat Computation of W0m method
@date Created on Tue Aug 07 14:25:11 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import sin


def comp_W0m(self):
    """Compute (or return) W0 in [m]

    Parameters
    ----------
    self : SlotMFlat
        A SlotMFlat object

    Returns
    -------
    W0m: float
        W0 in [m]

    """

    Rbo = self.get_Rbo()
    if self.W0_is_rad:  # Convert W0 to m
        return 2 * Rbo * sin((self.W0 / 2))
    else:
        return self.W0
