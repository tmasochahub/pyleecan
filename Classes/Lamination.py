# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import check_init_dict, check_var
from pyleecan.Functions.save import save
from pyleecan.Classes.frozen import FrozenClass

from pyleecan.Methods.Machine.Lamination.build_geometry import build_geometry
from pyleecan.Methods.Machine.Lamination.check import check
from pyleecan.Methods.Machine.Lamination.comp_length import comp_length
from pyleecan.Methods.Machine.Lamination.comp_masses import comp_masses
from pyleecan.Methods.Machine.Lamination.comp_radius_mec import comp_radius_mec
from pyleecan.Methods.Machine.Lamination.comp_surface_axial_vent import (
    comp_surface_axial_vent,
)
from pyleecan.Methods.Machine.Lamination.comp_surfaces import comp_surfaces
from pyleecan.Methods.Machine.Lamination.comp_volumes import comp_volumes
from pyleecan.Methods.Machine.Lamination.get_bore_line import get_bore_line
from pyleecan.Methods.Machine.Lamination.get_Rbo import get_Rbo
from pyleecan.Methods.Machine.Lamination.get_Ryoke import get_Ryoke
from pyleecan.Methods.Machine.Lamination.get_name_phase import get_name_phase
from pyleecan.Methods.Machine.Lamination.plot import plot
from pyleecan.Methods.Machine.Lamination.comp_output_geo import comp_output_geo
from pyleecan.Methods.Machine.Lamination.get_polar_eq import get_polar_eq

from pyleecan.Classes.check import InitUnKnowClassError
from pyleecan.Classes.Material import Material
from pyleecan.Classes.Hole import Hole
from pyleecan.Classes.HoleMag import HoleMag
from pyleecan.Classes.HoleM50 import HoleM50
from pyleecan.Classes.HoleM51 import HoleM51
from pyleecan.Classes.HoleM52 import HoleM52
from pyleecan.Classes.HoleM53 import HoleM53
from pyleecan.Classes.HoleM54 import HoleM54
from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.Classes.VentilationPolar import VentilationPolar
from pyleecan.Classes.VentilationTrap import VentilationTrap


class Lamination(FrozenClass):
    """abstract class for lamination"""

    VERSION = 1

    # cf Methods.Machine.Lamination.build_geometry
    build_geometry = build_geometry
    # cf Methods.Machine.Lamination.check
    check = check
    # cf Methods.Machine.Lamination.comp_length
    comp_length = comp_length
    # cf Methods.Machine.Lamination.comp_masses
    comp_masses = comp_masses
    # cf Methods.Machine.Lamination.comp_radius_mec
    comp_radius_mec = comp_radius_mec
    # cf Methods.Machine.Lamination.comp_surface_axial_vent
    comp_surface_axial_vent = comp_surface_axial_vent
    # cf Methods.Machine.Lamination.comp_surfaces
    comp_surfaces = comp_surfaces
    # cf Methods.Machine.Lamination.comp_volumes
    comp_volumes = comp_volumes
    # cf Methods.Machine.Lamination.get_bore_line
    get_bore_line = get_bore_line
    # cf Methods.Machine.Lamination.get_Rbo
    get_Rbo = get_Rbo
    # cf Methods.Machine.Lamination.get_Ryoke
    get_Ryoke = get_Ryoke
    # cf Methods.Machine.Lamination.get_name_phase
    get_name_phase = get_name_phase
    # cf Methods.Machine.Lamination.plot
    plot = plot
    # cf Methods.Machine.Lamination.comp_output_geo
    comp_output_geo = comp_output_geo
    # cf Methods.Machine.Lamination.get_polar_eq
    get_polar_eq = get_polar_eq
    # save method is available in all object
    save = save

    def __init__(
        self,
        L1=0.35,
        mat_type=-1,
        Nrvd=0,
        Wrvd=0,
        Kf1=0.95,
        is_internal=True,
        Rint=0,
        Rext=1,
        is_stator=True,
        axial_vent=list(),
        init_dict=None,
    ):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if mat_type == -1:
            mat_type = Material()
        if init_dict is not None:  # Initialisation by dict
            check_init_dict(
                init_dict,
                [
                    "L1",
                    "mat_type",
                    "Nrvd",
                    "Wrvd",
                    "Kf1",
                    "is_internal",
                    "Rint",
                    "Rext",
                    "is_stator",
                    "axial_vent",
                ],
            )
            # Overwrite default value with init_dict content
            if "L1" in list(init_dict.keys()):
                L1 = init_dict["L1"]
            if "mat_type" in list(init_dict.keys()):
                mat_type = init_dict["mat_type"]
            if "Nrvd" in list(init_dict.keys()):
                Nrvd = init_dict["Nrvd"]
            if "Wrvd" in list(init_dict.keys()):
                Wrvd = init_dict["Wrvd"]
            if "Kf1" in list(init_dict.keys()):
                Kf1 = init_dict["Kf1"]
            if "is_internal" in list(init_dict.keys()):
                is_internal = init_dict["is_internal"]
            if "Rint" in list(init_dict.keys()):
                Rint = init_dict["Rint"]
            if "Rext" in list(init_dict.keys()):
                Rext = init_dict["Rext"]
            if "is_stator" in list(init_dict.keys()):
                is_stator = init_dict["is_stator"]
            if "axial_vent" in list(init_dict.keys()):
                axial_vent = init_dict["axial_vent"]
        # Initialisation by argument
        self.parent = None
        self.L1 = L1
        # mat_type can be None, a Material object or a dict
        if isinstance(mat_type, dict):
            self.mat_type = Material(init_dict=mat_type)
        else:
            self.mat_type = mat_type
        self.Nrvd = Nrvd
        self.Wrvd = Wrvd
        self.Kf1 = Kf1
        self.is_internal = is_internal
        self.Rint = Rint
        self.Rext = Rext
        self.is_stator = is_stator
        # axial_vent can be None or a list of Hole object
        self.axial_vent = list()
        if type(axial_vent) is list:
            for obj in axial_vent:
                if obj is None:  # Default value
                    self.axial_vent.append(Hole())
                elif isinstance(obj, dict):
                    # Call the correct constructor according to the dict
                    load_dict = {
                        "HoleMag": HoleMag,
                        "HoleM50": HoleM50,
                        "HoleM51": HoleM51,
                        "HoleM52": HoleM52,
                        "HoleM53": HoleM53,
                        "HoleM54": HoleM54,
                        "VentilationCirc": VentilationCirc,
                        "VentilationPolar": VentilationPolar,
                        "VentilationTrap": VentilationTrap,
                        "Hole": Hole,
                    }
                    obj_class = obj.get("__class__")
                    if obj_class is None:
                        self.axial_vent.append(Hole(init_dict=obj))
                    elif obj_class in list(load_dict.keys()):
                        self.axial_vent.append(load_dict[obj_class](init_dict=obj))
                    else:  # Avoid generation error or wrong modification in json
                        raise InitUnKnowClassError(
                            "Unknow class name in init_dict for axial_vent"
                        )
                else:
                    self.axial_vent.append(obj)
        elif axial_vent is None:
            self.axial_vent = list()
        else:
            self.axial_vent = axial_vent

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Lamination_str = ""
        if self.parent is None:
            Lamination_str += "parent = None " + linesep
        else:
            Lamination_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Lamination_str += "L1 = " + str(self.L1) + linesep
        Lamination_str += (
            "mat_type = " + str(self.mat_type.as_dict()) + linesep + linesep
        )
        Lamination_str += "Nrvd = " + str(self.Nrvd) + linesep
        Lamination_str += "Wrvd = " + str(self.Wrvd) + linesep
        Lamination_str += "Kf1 = " + str(self.Kf1) + linesep
        Lamination_str += "is_internal = " + str(self.is_internal) + linesep
        Lamination_str += "Rint = " + str(self.Rint) + linesep
        Lamination_str += "Rext = " + str(self.Rext) + linesep
        Lamination_str += "is_stator = " + str(self.is_stator) + linesep
        if len(self.axial_vent) == 0:
            Lamination_str += "axial_vent = []"
        for ii in range(len(self.axial_vent)):
            Lamination_str += (
                "axial_vent["
                + str(ii)
                + "] = "
                + str(self.axial_vent[ii].as_dict())
                + "\n"
            )
        return Lamination_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.L1 != self.L1:
            return False
        if other.mat_type != self.mat_type:
            return False
        if other.Nrvd != self.Nrvd:
            return False
        if other.Wrvd != self.Wrvd:
            return False
        if other.Kf1 != self.Kf1:
            return False
        if other.is_internal != self.is_internal:
            return False
        if other.Rint != self.Rint:
            return False
        if other.Rext != self.Rext:
            return False
        if other.is_stator != self.is_stator:
            return False
        if other.axial_vent != self.axial_vent:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Lamination_dict = dict()
        Lamination_dict["L1"] = self.L1
        if self.mat_type is None:
            Lamination_dict["mat_type"] = None
        else:
            Lamination_dict["mat_type"] = self.mat_type.as_dict()
        Lamination_dict["Nrvd"] = self.Nrvd
        Lamination_dict["Wrvd"] = self.Wrvd
        Lamination_dict["Kf1"] = self.Kf1
        Lamination_dict["is_internal"] = self.is_internal
        Lamination_dict["Rint"] = self.Rint
        Lamination_dict["Rext"] = self.Rext
        Lamination_dict["is_stator"] = self.is_stator
        Lamination_dict["axial_vent"] = list()
        for obj in self.axial_vent:
            Lamination_dict["axial_vent"].append(obj.as_dict())
        # The class name is added to the dict fordeserialisation purpose
        Lamination_dict["__class__"] = "Lamination"
        return Lamination_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.L1 = None
        if self.mat_type is not None:
            self.mat_type._set_None()
        self.Nrvd = None
        self.Wrvd = None
        self.Kf1 = None
        self.is_internal = None
        self.Rint = None
        self.Rext = None
        self.is_stator = None
        for obj in self.axial_vent:
            obj._set_None()

    def _get_L1(self):
        """getter of L1"""
        return self._L1

    def _set_L1(self, value):
        """setter of L1"""
        check_var("L1", value, "float", Vmin=0, Vmax=100)
        self._L1 = value

    # Lamination stack active length [m] without radial ventilation airducts but including insulation layers between lamination sheets
    # Type : float, min = 0, max = 100
    L1 = property(
        fget=_get_L1,
        fset=_set_L1,
        doc=u"""Lamination stack active length [m] without radial ventilation airducts but including insulation layers between lamination sheets""",
    )

    def _get_mat_type(self):
        """getter of mat_type"""
        return self._mat_type

    def _set_mat_type(self, value):
        """setter of mat_type"""
        check_var("mat_type", value, "Material")
        self._mat_type = value

        if self._mat_type is not None:
            self._mat_type.parent = self

    # Lamination's material
    # Type : Material
    mat_type = property(
        fget=_get_mat_type, fset=_set_mat_type, doc=u"""Lamination's material"""
    )

    def _get_Nrvd(self):
        """getter of Nrvd"""
        return self._Nrvd

    def _set_Nrvd(self, value):
        """setter of Nrvd"""
        check_var("Nrvd", value, "int", Vmin=0)
        self._Nrvd = value

    # number of radial air ventilation ducts in lamination
    # Type : int, min = 0
    Nrvd = property(
        fget=_get_Nrvd,
        fset=_set_Nrvd,
        doc=u"""number of radial air ventilation ducts in lamination """,
    )

    def _get_Wrvd(self):
        """getter of Wrvd"""
        return self._Wrvd

    def _set_Wrvd(self, value):
        """setter of Wrvd"""
        check_var("Wrvd", value, "float", Vmin=0)
        self._Wrvd = value

    # axial width of ventilation ducts in lamination
    # Type : float, min = 0
    Wrvd = property(
        fget=_get_Wrvd,
        fset=_set_Wrvd,
        doc=u"""axial width of ventilation ducts in lamination""",
    )

    def _get_Kf1(self):
        """getter of Kf1"""
        return self._Kf1

    def _set_Kf1(self, value):
        """setter of Kf1"""
        check_var("Kf1", value, "float", Vmin=0, Vmax=1)
        self._Kf1 = value

    # lamination stacking / packing factor
    # Type : float, min = 0, max = 1
    Kf1 = property(
        fget=_get_Kf1, fset=_set_Kf1, doc=u"""lamination stacking / packing factor"""
    )

    def _get_is_internal(self):
        """getter of is_internal"""
        return self._is_internal

    def _set_is_internal(self, value):
        """setter of is_internal"""
        check_var("is_internal", value, "bool")
        self._is_internal = value

    # 1 for internal lamination topology, 0 for external lamination
    # Type : bool
    is_internal = property(
        fget=_get_is_internal,
        fset=_set_is_internal,
        doc=u"""1 for internal lamination topology, 0 for external lamination""",
    )

    def _get_Rint(self):
        """getter of Rint"""
        return self._Rint

    def _set_Rint(self, value):
        """setter of Rint"""
        check_var("Rint", value, "float", Vmin=0)
        self._Rint = value

    # To fill
    # Type : float, min = 0
    Rint = property(fget=_get_Rint, fset=_set_Rint, doc=u"""To fill""")

    def _get_Rext(self):
        """getter of Rext"""
        return self._Rext

    def _set_Rext(self, value):
        """setter of Rext"""
        check_var("Rext", value, "float", Vmin=0)
        self._Rext = value

    # To fill
    # Type : float, min = 0
    Rext = property(fget=_get_Rext, fset=_set_Rext, doc=u"""To fill""")

    def _get_is_stator(self):
        """getter of is_stator"""
        return self._is_stator

    def _set_is_stator(self, value):
        """setter of is_stator"""
        check_var("is_stator", value, "bool")
        self._is_stator = value

    # To fill
    # Type : bool
    is_stator = property(fget=_get_is_stator, fset=_set_is_stator, doc=u"""To fill""")

    def _get_axial_vent(self):
        """getter of axial_vent"""
        for obj in self._axial_vent:
            if obj is not None:
                obj.parent = self
        return self._axial_vent

    def _set_axial_vent(self, value):
        """setter of axial_vent"""
        check_var("axial_vent", value, "[Hole]")
        self._axial_vent = value

        for obj in self._axial_vent:
            if obj is not None:
                obj.parent = self

    # Axial ventilation ducts
    # Type : [Hole]
    axial_vent = property(
        fget=_get_axial_vent, fset=_set_axial_vent, doc=u"""Axial ventilation ducts"""
    )
