import sys
sys.path.append('/home/derek/Documents/UoG/GA1/FPSE/AdapterSSversion')
from src.Rummy import Rummy
from src.PlayingCard import PlayingCard
from src.TestInput import TestInput
import unittest

class TestRummy(unittest.TestCase):

    rummy = Rummy()
    playing_card = PlayingCard()
    test_input = TestInput()

    def setUp(self):
        self.deck = []
        for suit in ['H', 'D', 'S', 'C']:
            for value in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                self.deck.append(suit + value)

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
        self.assertEqual(self.deck, self.playing_card.generate_deck())


    def test_getNumberFromPlayer(self):





# if __name__ == '__main__':
#     unittest.main()
