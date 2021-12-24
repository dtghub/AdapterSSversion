import sys
sys.path.append('/home/derek/Documents/UoG/GA1/FPSE/AdapterSSversion')
from src.Rummy import Rummy
from src.PlayingCard import PlayingCard
from src.TestInput import TestInput
from src.TestOutput import TestOutput
import unittest

class TestRummy(unittest.TestCase):

    rummy = Rummy()
    playing_card = PlayingCard()
    test_input = TestInput()
    test_output = TestOutput()

    @classmethod
    def setUpClass(cls):
        cls.deck = []
        # a full deck, unshuffled
        for suit in ['H', 'D', 'S', 'C']:
            for value in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                cls.deck.append(suit + value)

    def setUp(self):
        self.test_output.reset_list_of_test_outputs()
     

    # def test_rummy(self):
    #     self.test_input.set_list_of_test_inputs([3,"T","S"])
    #     self.rummy.main()

    # def test_valid_deal_input(self):
    #     self.test_input.set_list_of_test_inputs(["T","S"])
    #     self.assertEqual("T",self.rummy.valid_deal_input())


    # Test correct number of cards
    def test_setupNewDeck_Length(self):
        newDeck = self.rummy.setupNewDeck()
        self.assertEqual(len(newDeck), 52)


    # Test all of the cards are in the shuffled deck
    def test_setupNewDeck_HasAllCards(self):
        newDeck = self.rummy.setupNewDeck()
        for eachCard in self.deck:
            cardInNewDeck = eachCard in newDeck
            self.assertTrue(cardInNewDeck)   

    # Test cards are shuffled at all
    def test_setupNewDeck_IsShuffled(self):
        newDeck = self.rummy.setupNewDeck()
        self.assertNotEqual(newDeck, self.deck)

        # Just in case...
    def test_generate_deck(self):
        self.assertEqual(self.deck, self.playing_card.generate_deck())


    # def test_getNumberFromPlayer(self):
    #     self.test_input.set_list_of_test_inputs(["S"])
    #     self.rummy.set_game_input(self.test_input)


    def test_askYorN_y(self):
        self.rummy.set_game_output(self.test_output)
        self.test_input.set_list_of_test_inputs(["y"])
        self.rummy.set_game_input(self.test_input)
        self.assertTrue(self.rummy.askYorN("Howdy"))
        temp = self.test_output.get_list_of_test_outputs()
        self.assertEquals(temp, [])

    def test_askYorN_Y(self):
        self.rummy.set_game_output(self.test_output)
        self.test_input.set_list_of_test_inputs(["Y"])
        self.rummy.set_game_input(self.test_input)
        self.assertTrue(self.rummy.askYorN("Howdy"))
        temp = self.test_output.get_list_of_test_outputs()
        self.assertEquals(temp, [])




    def test_askYorN_lpo_n(self):
        self.rummy.set_game_output(self.test_output)
        self.test_input.set_list_of_test_inputs(["lpo","n"])
        self.rummy.set_game_input(self.test_input)
        self.assertFalse(self.rummy.askYorN("Howdy"))
        temp = self.test_output.get_list_of_test_outputs()
        # print("reply:", temp)
        self.assertEquals(temp[0], "Please enter 'y' or 'n'")


    def test_askYorN__N(self):
        self.rummy.set_game_output(self.test_output)
        self.test_input.set_list_of_test_inputs(["","N"])
        self.rummy.set_game_input(self.test_input)
        self.assertFalse(self.rummy.askYorN("Howdy"))
        temp = self.test_output.get_list_of_test_outputs()
        # print("reply:", temp)
        self.assertEquals(temp[0], "Please enter 'y' or 'n'")



if __name__ == '__main__':
    unittest.main()
