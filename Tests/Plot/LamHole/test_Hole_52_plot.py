# -*- coding: utf-8 -*-
"""
@date Created on Wed Jan 13 17:45:15 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

from os.path import join
from unittest import TestCase

import matplotlib.pyplot as plt
from numpy import pi

from pyleecan.Classes.Frame import Frame
from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.Lamination import Lamination
from pyleecan.Classes.Machine import Machine
from pyleecan.Classes.Magnet import Magnet
from pyleecan.Classes.Shaft import Shaft
from pyleecan.Classes.HoleM52 import HoleM52
from pyleecan.Tests import save_plot_path as save_path


class test_Hole_52_plot(TestCase):
    """unittest for Lamination with Hole 52 plot"""

    def setUp(self):
        """Run at the begining of every test to setup the machine"""
        plt.close("all")
        test_obj = Machine()
        test_obj.rotor = LamHole(
            Rint=45e-3 / 2, Rext=81.5e-3, is_stator=False, is_internal=True, L1=0.9
        )
        test_obj.rotor.hole = list()
        test_obj.rotor.hole.append(
            HoleM52(Zh=8, W0=27e-3, W3=16.2e-3, H0=1e-3, H1=5e-3, H2=1e-3)
        )
        test_obj.shaft = Shaft(Drsh=test_obj.rotor.Rint * 2, Lshaft=1.2)

        test_obj.stator = Lamination(
            Rint=0.09, Rext=0.12, is_internal=False, is_stator=True, L1=0.9
        )
        test_obj.frame = Frame(Rint=0.12, Rext=0.12, Lfra=0.7)
        self.test_obj = test_obj

    def test_Lam_Hole_52(self):
        """Test machine plot hole 52 with magnet
        """
        self.test_obj.plot()
        fig = plt.gcf()
        # Rotor + 2 for stator + 0 for frame + 1 for shaft
        self.assertEqual(len(fig.axes[0].patches), 29)
        fig.savefig(join(save_path, "test_Lam_Hole_s52_1-Machine.png"))

        self.test_obj.rotor.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_Lam_Hole_s52_2-Rotor.png"))
        # 2 for lam + 3*8 for holes
        self.assertEqual(len(fig.axes[0].patches), 26)

    def test_Lam_Hole_52_no_mag(self):
        """Test machine plot hole 52 without magnet
        """
        self.test_obj.rotor.hole[0].magnet_0 = None
        self.test_obj.rotor.plot()
        fig = plt.gcf()
        # 2 for lam + 1*8 for holes
        self.assertEqual(len(fig.axes[0].patches), 10)
        fig.savefig(
            join(save_path, "test_Lam_Hole_s52_3-Rotor hole without " "magnet.png")
        )
