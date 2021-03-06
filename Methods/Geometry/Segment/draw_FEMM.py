# -*- coding: utf-8 -*-
"""@package draw_FEMM
@date Created on juil. 30 15:31 2018
@author franco_i
"""

import femm

from pyleecan.Functions.FEMM import boundary_prop


def draw_FEMM(
    self,
    nodeprop=None,
    propname=None,
    elementsize=None,
    automesh=None,
    hide=False,
    group=None,
):
    """<   Draw the segment in FEMM and assign the property

    Parameters
    ----------
    nodeprop :
        Nodal property
         (Default value = None)
    propname :
        Boundary property ’propname’
         (Default value = None)
    elementsize :
        Local element size along segment no greater than elementsize
         (Default value = None)
    automesh :
        0 = mesher defers to the element constraint defined by
        elementsize, 1 = mesher automatically chooses mesh size along
        the selected segments
        (Default value = None)
    hide :
        0 = not hidden in post-processor, 1 == hidden in post processorc
         (Default value = False)
    group :
        group the segment belongs
         (Default value = None)

    Returns
    -------

    
    """

    # Get BC (if any)
    if self.label in boundary_prop:
        propname = boundary_prop[self.label]

    # Add the nodes
    X1, Y1 = self.begin.real, self.begin.imag
    X2, Y2 = self.end.real, self.end.imag
    femm.mi_addnode(X1, Y1)
    femm.mi_selectnode(X1, Y1)
    femm.mi_setnodeprop(nodeprop, group)
    femm.mi_clearselected()
    femm.mi_addnode(X2, Y2)
    femm.mi_selectnode(X2, Y2)
    femm.mi_setnodeprop(nodeprop, group)
    femm.mi_clearselected()
    # add the segment
    femm.mi_addsegment(X1, Y1, X2, Y2)
    # Set property
    femm.mi_selectsegment((X1 + X2) / 2, (Y1 + Y2) / 2)
    femm.mi_setsegmentprop(propname, elementsize, automesh, hide, group)
    femm.mi_clearselected()
