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





    def test_checkForRun_NoRun(self):
        startPosition = 1
        playLength = 3
        playerHand = ['C03', 'D08', 'D10', 'D11', 'H04', 'H06', 'H11', 'H12', 'S01', 'S06']
        resultOfCheck = self.rummy.checkForRun(startPosition, playLength, playerHand)
        self.assertEquals(resultOfCheck, [])

    def test_checkForRun_YesRun_1_3(self):
        startPosition = 1
        playLength = 3
        playerHand = ['C03', 'D08', 'D09', 'D10', 'D11', 'H04', 'H06', 'H11', 'H12', 'S01']
        resultOfCheck = self.rummy.checkForRun(startPosition, playLength, playerHand)
        self.assertEquals(resultOfCheck, ['D08', 'D09', 'D10'])

    def test_checkForRun_NoRun_3_3(self):
        startPosition = 3
        playLength = 3
        playerHand = ['C03', 'D08', 'D09', 'D10', 'D11', 'H04', 'H06', 'H11', 'H12', 'S01']
        resultOfCheck = self.rummy.checkForRun(startPosition, playLength, playerHand)
        self.assertEquals(resultOfCheck, [])


    def test_checkForRun_YesRun_1_4(self):
        startPosition = 1
        playLength = 4
        playerHand = ['C03', 'D08', 'D09', 'D10', 'D11', 'H04', 'H06', 'H11', 'H12', 'S01']
        resultOfCheck = self.rummy.checkForRun(startPosition, playLength, playerHand)
        self.assertEquals(resultOfCheck, ['D08', 'D09', 'D10', 'D11'])



    def test_checkForSet_YesSet_3_3(self):
        startPosition = 3
        playLength = 3
        playerHand = ['C03', 'C04', 'D04', 'D08', 'D11', 'H04', 'H08', 'H11', 'S04', 'S08']
        resultOfCheck = self.rummy.checkForSet(startPosition, playLength, playerHand)
        self.assertEquals(resultOfCheck, ['D08', 'H08', 'S08'])

    def test_checkForSet_YesSet_1_3(self):
        startPosition = 1
        playLength = 3
        playerHand = ['C03', 'C04', 'D04', 'D08', 'D11', 'H04', 'H08', 'H11', 'S04', 'S08']
        resultOfCheck = self.rummy.checkForSet(startPosition, playLength, playerHand)
        self.assertEquals(resultOfCheck, ['C04', 'D04', 'H04'])


    def test_checkForSet_YesSet_1_4(self):
        startPosition = 1
        playLength = 4
        playerHand = ['C03', 'C04', 'D04', 'D08', 'D11', 'H04', 'H08', 'H11', 'S04', 'S08']
        resultOfCheck = self.rummy.checkForSet(startPosition, playLength, playerHand)
        self.assertEquals(resultOfCheck, ['C04', 'D04', 'H04', 'S04'])

    def test_checkForSet_NoSet_0_4(self):
        startPosition = 0
        playLength = 4
        playerHand = ['C03', 'C04', 'D04', 'D08', 'D11', 'H04', 'H08', 'H11', 'S04', 'S08']
        resultOfCheck = self.rummy.checkForSet(startPosition, playLength, playerHand)
        self.assertEquals(resultOfCheck, [])



    def test_findPlaysInHand(self):
        listOfPlays = {'playerHand': ['C03', 'C04', 'D04', 'D08', 'D11', 'H04', 'H08', 'H11', 'S04', 'S08'], 'playsFound': [], 'newPlaysFound': [], 'playsMadeSoFar': [], 'bestScoreSoFar': 0}
        resultOfCheck = self.rummy.findPlaysInHand(listOfPlays)
        self.assertEquals(resultOfCheck['newPlaysFound'], [['C04', 'D04', 'H04'], ['D04', 'H04', 'S04'], ['D08', 'H08', 'S08'], ['C04', 'D04', 'H04', 'S04']])




    def test_findPlaysInHand2(self):
        listOfPlays = {'playerHand': ['C03', 'C04', 'C05', 'D04', 'D08', 'D11', 'H04', 'H08', 'H11', 'S04', 'S08'], 'playsFound': [], 'newPlaysFound': [], 'playsMadeSoFar': [], 'bestScoreSoFar': 0}
        resultOfCheck = self.rummy.findPlaysInHand(listOfPlays)
        self.assertEquals(resultOfCheck['newPlaysFound'], [['C03', 'C04', 'C05'], ['C04', 'D04', 'H04'], ['D04', 'H04', 'S04'], ['D08', 'H08', 'S08'], ['C04', 'D04', 'H04', 'S04']])



    def test_findPlaysInHand_MeldSet(self):
        listOfPlays = {'playerHand': ['C03', 'C04', 'C05', 'D04', 'D08', 'D11', 'H04', 'H08', 'H11', 'S04', 'S08'], 'playsFound': [['D05', 'H05', 'S05']], 'newPlaysFound': [], 'playsMadeSoFar': [], 'bestScoreSoFar': 0}
        resultOfCheck = self.rummy.findPlaysInHand(listOfPlays)
        self.assertEquals(resultOfCheck['newPlaysFound'], [['C03', 'C04', 'C05'], ['C04', 'D04', 'H04'], ['D04', 'H04', 'S04'], ['D08', 'H08', 'S08'], ['C04', 'D04', 'H04', 'S04'], [['C05'], ['D05', 'H05', 'S05', 'C05'], ['D05', 'H05', 'S05']]])

    def test_findPlaysInHand_MeldSet(self):
        listOfPlays = {'playerHand': ['C03', 'C04', 'C05', 'D04', 'D08', 'H03', 'H04', 'H08', 'H11', 'S04', 'S08'], 'playsFound': [['D09', 'D10', 'D11']], 'newPlaysFound': [], 'playsMadeSoFar': [], 'bestScoreSoFar': 0}
        resultOfCheck = self.rummy.findPlaysInHand(listOfPlays)
        self.assertEquals(resultOfCheck['newPlaysFound'], [['C03', 'C04', 'C05'], ['C04', 'D04', 'H04'], ['D04', 'H04', 'S04'], ['D08', 'H08', 'S08'], ['C04', 'D04', 'H04', 'S04'], [['D08'], ['D08', 'D09', 'D10', 'D11'], ['D09', 'D10', 'D11']]])





if __name__ == '__main__':
    unittest.main()
