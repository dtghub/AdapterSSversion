import sys
sys.path.append('/home/derek/Documents/UoG/GA1/FPSE/AdapterSSversion')
from abc import ABC, abstractmethod

class Input(ABC):
    def get_string(self, message):
        pass