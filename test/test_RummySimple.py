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

        cls.rummy.set_game_output(cls.test_output)
        cls.rummy.set_game_input(cls.test_input)


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
        self.test_input.set_list_of_test_inputs(["y"])
        self.assertTrue(self.rummy.askYorN("Howdy"))
        outputs = self.test_output.get_list_of_test_outputs()
        self.assertEquals(outputs, [])

    def test_askYorN_Y(self):
        self.test_input.set_list_of_test_inputs(["Y"])
        self.assertTrue(self.rummy.askYorN("Howdy"))
        outputs = self.test_output.get_list_of_test_outputs()
        self.assertEquals(outputs, [])


    def test_askYorN_lpo_n(self):
        self.test_input.set_list_of_test_inputs(["lpo"," ","n"])
        self.assertFalse(self.rummy.askYorN("Howdy"))
        outputs = self.test_output.get_list_of_test_outputs()
        self.assertEquals(outputs[0], ["Please enter 'y' or 'n'"])
        self.assertEquals(outputs[1], ["Please enter 'y' or 'n'"])


    def test_askYorN__N(self):
        self.test_input.set_list_of_test_inputs(["","N"])
        self.assertFalse(self.rummy.askYorN("Howdy"))
        outputs = self.test_output.get_list_of_test_outputs()
        self.assertEquals(outputs[0], ["Please enter 'y' or 'n'"])






    def test_getNumberFromPlayer_3(self):
        self.test_input.set_list_of_test_inputs(["3"])
        self.assertEquals(self.rummy.getNumberFromPlayer("Please enter yer munber, sah!", 2, 5, 2), 3)
        outputs = self.test_output.get_list_of_test_outputs()
        self.assertEquals(outputs, [])

    def test_getNumberFromPlayer_1_100_4(self):
        self.test_input.set_list_of_test_inputs(["1", "100", "4"])
        self.assertEquals(self.rummy.getNumberFromPlayer("Please enter yer munber, sah!", 2, 5, 2), 4)
        outputs = self.test_output.get_list_of_test_outputs()
        self.assertEquals(outputs[0], ["Sorry, you need to enter a number, minimum; 2, maximum; 5"])
        self.assertEquals(outputs[1], ["Sorry, you need to enter a number, minimum; 2, maximum; 5"])



    def test_getNumberFromPlayer_1000_m1_5(self):
        self.test_input.set_list_of_test_inputs(["1000", "-1", "5"])
        self.assertEquals(self.rummy.getNumberFromPlayer("Please enter yer munber, sah!", 2, 5, 2), 5)
        outputs = self.test_output.get_list_of_test_outputs()
        self.assertEquals(outputs[0], ["Sorry, you need to enter a number, minimum; 2, maximum; 5"])
        

    # Sorry, you need to enter a number, minimum; 2, maximum; 5





    def tst_






if __name__ == '__main__':
    unittest.main()
