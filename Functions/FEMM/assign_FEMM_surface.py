# -*- coding: utf-8 -*-
"""@package assign_FEMM_Machine_part
@date Created on août 09 14:12 2018
@author franco_i
@todo "Radial" magnetization for HoleMx-Class
"""
import femm
from numpy import angle, pi, floor_divide
from pyleecan.Classes.HoleM50 import HoleM50
from pyleecan.Classes.HoleM51 import HoleM51
from pyleecan.Classes.HoleM52 import HoleM52
from pyleecan.Classes.HoleM53 import HoleM53
from pyleecan.Methods import NotImplementedYetError


def assign_FEMM_surface(surf, prop, mesh_dict, rotor, stator):
    """Assign the property given in parameter to surface having the label given
    Parameters
    ----------
    surf : Surface
        the surface to assign
    prop : str
        The property to assign in FEMM
    mesh_dict : dict
        Dictionnary containing the mesh parameters corresponding to the surface
    rotor : Lamination
        The rotor of the machine
    stator : Lamination
        The stator of the machine
    Returns
    -------
    None
    
    """
    label = surf.label
    Clabel = 0  # By default no circuit
    Ntcoil = 0  # By default no circuit
    mag = 0  # By default no magnetization

    # Select the lamination according to the label
    if "Rotor" in label:
        lam = rotor
    else:
        lam = stator

    # point_ref is None => don't assign the surface
    if surf.point_ref is not None:
        # Select the surface
        point_ref = surf.point_ref
        femm.mi_addblocklabel(point_ref.real, point_ref.imag)
        femm.mi_selectlabel(point_ref.real, point_ref.imag)

        # Get circuit or magnetization properties if needed
        if "Wind" in label:  # If the surface is a winding
            if "Rotor" in label:  # Winding on the rotor
                Clabel = "Circr" + prop[2]
            else:  # winding on the stator
                Clabel = "Circs" + prop[2]
            Ntcoil = lam.winding.Ntcoil
            if prop[-1] == "-":  # Adapt Ntcoil sign if needed
                Ntcoil *= -1
        elif "HoleMagnet" in label:  # LamHole
            if "Parallel" in label:
                # calculate pole angle and angle of pole middle
                alpha_p = 360 / lam.hole[0].Zh
                mag_0 = (
                    floor_divide(angle(point_ref, deg=True), alpha_p) + 0.5
                ) * alpha_p

                # HoleM50 or HoleM53
                if (type(lam.hole[0]) == HoleM50) or (type(lam.hole[0]) == HoleM53):
                    if "_T0_" in label:
                        mag = mag_0 + lam.hole[0].comp_alpha() * 180 / pi
                    else:
                        mag = mag_0 - lam.hole[0].comp_alpha() * 180 / pi

                # HoleM51
                if type(lam.hole[0]) == HoleM51:
                    if "_T0_" in label:
                        mag = mag_0 + lam.hole[0].comp_alpha() * 180 / pi
                    elif "_T1_" in label:
                        mag = mag_0
                    else:
                        mag = mag_0 - lam.hole[0].comp_alpha() * 180 / pi

                # HoleM52
                if type(lam.hole[0]) == HoleM52:
                    mag = mag_0

                # modifiy magnetisation of south poles
                if "_S_" in label:
                    mag = mag + 180
            else:
                raise NotImplementedYetError(
                    "Only parallele magnetization are available for HoleMagnet"
                )
        elif "Magnet" in label:  # LamSlotMag
            if "Radial" in label and "_N_" in label:  # Radial magnetization
                mag = "theta"  # North pole magnet
            elif "Radial" in label:
                mag = "theta + 180"  # South pole magnet
            elif "Parallel" in label and "_N_" in label:
                mag = angle(point_ref) * 180 / pi  # North pole magnet
            elif "Parallel" in label:
                mag = angle(point_ref) * 180 / pi + 180  # South pole magnet
        elif "Ventilation" in label:
            prop = "Air"
        elif "Hole" in label:
            prop = "Air"
        # Set the surface property
        femm.mi_setblockprop(
            prop,
            mesh_dict["automesh"],
            mesh_dict["meshsize"],
            Clabel,
            mag,
            mesh_dict["group"],
            Ntcoil,
        )
        femm.mi_clearselected()
