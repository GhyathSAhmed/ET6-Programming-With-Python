import unittest

from ..add import add

class TestMystery1(unittest.TestCase):
    """ """

    def test_minimal_input(self):
        """"""
        self.assertEqual(add(0, 0), 0)
