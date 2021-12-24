import sys
sys.path.append('/home/derek/Documents/UoG/GA1/FPSE/AdapterSSversion')
from src.Output import Output

class TestOutput(Output):

    list_of_test_outputs = []

    #allows e.g. list to be reset to []
    def set_list_of_test_outputs(self, test_output):
        self.list_of_test_outputs = test_output

    def display(self, *message):
        self.list_of_test_outputs.append(*message)
        return self.list_of_test_outputs
        