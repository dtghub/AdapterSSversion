import sys
sys.path.append('/home/derek/Documents/UoG/GA1/FPSE/AdapterSSversion')
from src.Output import Output

class TestOutput(Output):

    list_of_test_outputs = []

    #allows e.g. list to be reset to []
    def get_list_of_test_outputs(self):
        return self.list_of_test_outputs

    def display(self, *message):
        self.list_of_test_outputs.append(*message)
        
        