import sys
sys.path.append('/home/derek/Documents/UoG/GA1/FPSE/AdapterSSversion')
from src.Input import Input
import unittest
class ConsoleInput(Input):

    def get_string(self, message):
        return input(message)