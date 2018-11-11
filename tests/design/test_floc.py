# from pytest import approx
#
# from aguaclara.design.floc import Flocculator
# from aguaclara.core.units import unit_registry as u
#
#
# def test_all_functions(utils):
#     floc = Flocculator(q=(20 * (u.L/u.s)), temp=(25 * u.degC))
#
#     tests = zip(
#         (floc.vel_gradient_avg, 118.715*(u.s**-1), 0.001),
#         (floc.vol, 6.233*(u.m**3), 0.001),
#         (floc.w_min_h_s_ratio, 0.1074*u.cm, 0.0001),
#         (floc.expansion_h_max, 0.375*u.m, 0.001),
#         (floc.baffles_s, 0.063*u.m, 0.001)
#     )
#
#     assert floc.channel_n == 2
#     assert floc.baffles_n == approx(31, 1)
#     utils.vaue(tests)

import unittest

from aguaclara.design.floc import Flocculator
from aguaclara.core.units import unit_registry as u


class FlocTest(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        self.floc = Flocculator()

    def test_vel_gradient_avg(self):
        self.assertAlmostEqual(self.floc.vel_gradient_avg, 118.715 * (u.s ** -1))
