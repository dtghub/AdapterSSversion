from src.Rummy import Rummy
from src.TestInput import TestInput
import unittest

class TestBlackJack(unittest.TestCase):

    rummy = Rummy()
    test_input = TestInput()

    def setUp(self):
        self.rummy.setGameInput(self.test_input)

    def test_rummy(self):
        self.test_input.set_list_of_test_inputs([3,"T","S"])
        self.rummy.main()

    def test_valid_deal_input(self):
        self.test_input.set_list_of_test_inputs(["T","S"])
        self.assertEqual("T",self.rummy.valid_deal_input())


