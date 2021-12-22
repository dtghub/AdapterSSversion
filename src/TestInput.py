from src.Input import Input

class TestInput(Input):

    list_of_test_inputs = []

    def set_list_of_test_inputs(self,test_inputs):
        self.list_of_test_inputs = test_inputs

    def getString(self, message):
        return self.list_of_test_inputs.pop(0)