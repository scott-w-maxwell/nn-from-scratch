class Layer:
    def __init__(self):

        self.input = None
        self.output = None

    # calculates the output Y of a layer for a given input X
    def forward_propagation(self, input):
    	pass

    # calculates dE/dX for a given dE/dY  (updates the parameters if any)
    def backward_propagation(self, output_error, learning_rate):
    	pass
