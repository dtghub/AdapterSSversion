import unittest
from os import listdir
from os.path import isfile, join
import sys
sys.path.append('/home/derek/Documents/UoGGA1/ProfLectures1/Week7/PythonStateChallenge/PythonCardGameStateStart')

class OneFileTest(unittest.TestCase):

    files = []

    def setUp(self):
        src_path = "./src"
        self.files = [file for file in listdir(src_path) if isfile(join(src_path, file))]
        # print("displaying self.files: ", self.files)

    def test_PlayerState(self):
        self.assertTrue("PlayerState.py" in self.files)
        # self.assertTrue(True)

    def test_ReadyToPlayState(self):
        self.assertTrue("ReadyToPlayState.py" in self.files)

    def test_StickState(self):
        self.assertTrue("StickState.py" in self.files)

    def test_TwistState(self):
        self.assertTrue("TwistState.py" in self.files)

    def test_EndState(self):
        self.assertTrue("EndState.py" in self.files)


if __name__ == '__main__':
    unittest.main()
