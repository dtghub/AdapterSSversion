import sys
sys.path.append('/home/derek/Documents/UoG/GA1/FPSE/AdapterSSversion')
from src.Output import Output
import unittest
class ConsoleOutput(Output):
    # print() accepts a variable number of parameters
    def display(self, *message):
        return print(*message)