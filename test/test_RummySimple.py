import sys
sys.path.append('/home/derek/Documents/UoG/GA1/FPSE/AdapterSSversion')
from src.Rummy import Rummy
from src.PlayingCard import PlayingCard
from src.TestInput import TestInput
import unittest

class TestBlackJack(unittest.TestCase):

    rummy = Rummy()
    test_input = TestInput()

    # def setUp(self):
    #     self.rummy.setGameInput(self.test_input)

    # def test_rummy(self):
    #     self.test_input.set_list_of_test_inputs([3,"T","S"])
    #     self.rummy.main()

    # def test_valid_deal_input(self):
    #     self.test_input.set_list_of_test_inputs(["T","S"])
    #     self.assertEqual("T",self.rummy.valid_deal_input())

    def test_setupNewDeck(self):
        newDeck = self.rummy.setupNewDeck()
        self.assertEqual(len(newDeck), 52)


# if __name__ == '__main__':
#     unittest.main()
