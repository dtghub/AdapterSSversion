import sys
sys.path.append('/home/derek/Documents/UoG/GA1/FPSE/AdapterSSversion')
from abc import ABC, abstractmethod

class Output(ABC):
    def display(self, message):
        pass