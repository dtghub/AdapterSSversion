import sys
sys.path.append('/home/derek/Documents/UoG/GA1/FPSE/AdapterSSversion')
from src.Output import Output

class TestOutput(Output):

    def printed_string(self, message):
        return message