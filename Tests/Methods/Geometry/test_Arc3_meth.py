# -*- coding: utf-8 -*-
"""@package

@date Created on Wed May 04 11:46:18 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from unittest import TestCase
from ddt import ddt, data
from pyleecan.Classes.Arc3 import Arc3

from numpy import pi, exp, sqrt, linspace

# For AlmostEqual
DELTA = 1e-6


discretize_test = list()
# Dictionary to test discretize
discretize_test.append({"nb_point": 9, "begin": 2, "end": -2, "direc": False})
discretize_test[0]["result"] = 2 * exp(1j * linspace(0, -pi, 11))
discretize_test.append({"nb_point": 9, "begin": 2, "end": -2, "direc": True})
discretize_test[1]["result"] = 2 * exp(1j * linspace(0, pi, 11))
discretize_test.append({"nb_point": 9, "begin": 2j, "end": -2j, "direc": True})
discretize_test[2]["result"] = 2 * exp(1j * linspace(pi / 2, 3 * pi / 2, 11))

# Dictionary to test comp_length
comp_length_test = list()
comp_length_test.append({"begin": 2, "end": 0, "direc": True, "expect": pi})
comp_length_test.append(
    {
        "begin": 2 * exp(1j * 3 * pi / 4),
        "end": 2 * exp(1j * pi / 4),
        "direc": False,
        "expect": (sqrt(2) * pi),
    }
)
# Dictionary to test comp_radius
comp_radius_test = list()
comp_radius_test.append({"begin": 2, "end": 0, "direc": True, "expect": 1})
comp_radius_test.append(
    {
        "begin": 2 * exp(1j * 3 * pi / 4),
        "end": 2 * exp(1j * pi / 4),
        "direc": False,
        "expect": (sqrt(2)),
    }
)
# Dictionary to test get_center
comp_center_test = list()
comp_center_test.append({"begin": 2, "end": 0, "direc": True, "expect": 1})
comp_center_test.append(
    {
        "begin": 2 * exp(1j * 3 * pi / 4),
        "end": 2 * exp(1j * pi / 4),
        "direc": False,
        "expect": (sqrt(2) * 1j),
    }
)
comp_center_test.append({"begin": 2j, "end": -2j, "direc": True, "expect": 0})
comp_center_test.append({"begin": 2j, "end": -2j, "direc": False, "expect": 0})
# Dictionary to test get_middle
comp_mid_test = list()
comp_mid_test.append({"begin": 2, "end": 0, "direc": True, "expect": 1 + 1j})
comp_mid_test.append({"begin": 2, "end": 0, "direc": False, "expect": 1 - 1j})
comp_mid_test.append({"begin": 2j, "end": -2j, "direc": True, "expect": -2})
comp_mid_test.append({"begin": 2j, "end": -2j, "direc": False, "expect": 2})
# Dictionary to test rotation
comp_rotate_test = list()
comp_rotate_test.append(
    {
        "begin": 1,
        "end": 1j,
        "direc": True,
        "angle": pi / 2,
        "exp_begin": 1j,
        "exp_end": -1,
    }
)
comp_rotate_test.append(
    {
        "begin": 1,
        "end": 1j,
        "direc": False,
        "angle": pi / 2,
        "exp_begin": 1j,
        "exp_end": -1,
    }
)
comp_rotate_test.append(
    {
        "begin": 2j,
        "end": -2j,
        "direc": True,
        "angle": pi,
        "exp_begin": -2j,
        "exp_end": 2j,
    }
)
comp_rotate_test.append(
    {
        "begin": 1 + 1j,
        "end": -1 - 1j,
        "direc": False,
        "angle": -pi / 4,
        "exp_begin": sqrt(2),
        "exp_end": -sqrt(2),
    }
)
# Dictonary to test translation
comp_translate_test = list()
comp_translate_test.append(
    {
        "begin": 1,
        "end": 1j,
        "direc": True,
        "delta": 2,
        "exp_begin": 3,
        "exp_end": 2 + 1j,
    }
)
comp_translate_test.append(
    {
        "begin": 2 + 2j,
        "end": 1j,
        "direc": False,
        "delta": -3j,
        "exp_begin": 2 - 1j,
        "exp_end": -2j,
    }
)
comp_translate_test.append(
    {
        "begin": 1,
        "end": 1j,
        "direc": True,
        "delta": 2 + 2j,
        "exp_begin": 3 + 2j,
        "exp_end": 2 + 3j,
    }
)

get_angle_test = list()
get_angle_test.append(
    {
        "begin": 1 + 0j,
        "end": 0.5 + 0.5j,
        "direction": True,
        "is_deg": True,
        "exp_angle": 180.0,
    }
)
get_angle_test.append(
    {
        "begin": 1 + 0j,
        "end": 0.5 + 0.5j,
        "direction": True,
        "is_deg": False,
        "exp_angle": pi,
    }
)
get_angle_test.append(
    {"begin": 1 + 0j, "end": 0, "direction": False, "is_deg": True, "exp_angle": -180.0}
)


@ddt
class test_Arc3_meth(TestCase):
    """unittest for Arc3 methods"""

    @data(*discretize_test)
    def test_discretize(self, test_dict):
        """Check that you can discretize an arc3
        """
        arc = Arc3(
            begin=test_dict["begin"],
            end=test_dict["end"],
            is_trigo_direction=test_dict["direc"],
        )

        result = arc.discretize(test_dict["nb_point"])

        self.assertEqual(result.size, test_dict["result"].size)
        for i in range(0, result.size):
            a = result[i]
            b = test_dict["result"][i]
            self.assertAlmostEqual((a - b) / a, 0, delta=DELTA)

    @data(*comp_length_test)
    def test_comp_length(self, test_dict):
        """Check that you can compute the lenght of an arc3
        """
        arc = Arc3(
            begin=test_dict["begin"],
            end=test_dict["end"],
            is_trigo_direction=test_dict["direc"],
        )
        result = arc.comp_length()
        self.assertAlmostEqual(abs(result - test_dict["expect"]), 0)

    @data(*comp_radius_test)
    def test_comp_radius(self, test_dict):
        """Check that you can compute the radius of an arc3
        """
        arc = Arc3(
            begin=test_dict["begin"],
            end=test_dict["end"],
            is_trigo_direction=test_dict["direc"],
        )
        result = arc.comp_radius()
        self.assertAlmostEqual(abs(result - test_dict["expect"]), 0)

    @data(*comp_center_test)
    def test_get_center(self, test_dict):
        """Check that you can compute the center
        """
        arc = Arc3(
            begin=test_dict["begin"],
            end=test_dict["end"],
            is_trigo_direction=test_dict["direc"],
        )
        result = arc.get_center()
        self.assertAlmostEqual(abs(result - test_dict["expect"]), 0)

    @data(*comp_mid_test)
    def test_get_middle(self, test_dict):
        """Check that you can compute the middle
        """
        arc = Arc3(
            begin=test_dict["begin"],
            end=test_dict["end"],
            is_trigo_direction=test_dict["direc"],
        )
        result = arc.get_middle()
        self.assertAlmostEqual(abs(result - test_dict["expect"]), 0)

    @data(*comp_rotate_test)
    def test_rotate(self, test_dict):
        """Check that you can rotate an arc3
        """
        arc = Arc3(
            begin=test_dict["begin"],
            end=test_dict["end"],
            is_trigo_direction=test_dict["direc"],
        )
        arc.rotate(test_dict["angle"])
        self.assertAlmostEqual(abs(arc.begin - test_dict["exp_begin"]), 0)
        self.assertAlmostEqual(abs(arc.end - test_dict["exp_end"]), 0)

    @data(*comp_translate_test)
    def test_translate(self, test_dict):
        """Check that you can translate an arc3
        """
        arc = Arc3(
            begin=test_dict["begin"],
            end=test_dict["end"],
            is_trigo_direction=test_dict["direc"],
        )
        arc.translate(test_dict["delta"])
        self.assertAlmostEqual(abs(arc.begin - test_dict["exp_begin"]), 0)
        self.assertAlmostEqual(abs(arc.end - test_dict["exp_end"]), 0)

    @data(*get_angle_test)
    def test_get_angle(self, test_dict):
        """Check that the arc3 computed angle is correct
        """
        arc = Arc3(
            begin=test_dict["begin"],
            end=test_dict["end"],
            is_trigo_direction=test_dict["direction"],
        )
        result = arc.get_angle(test_dict["is_deg"])
        self.assertAlmostEqual(result, test_dict["exp_angle"])
