inputs = [1, 2, 3]
weights = [0.2, 0.8, -0.5]
bias = 2

# Single Neuron sums each input multiplied by that input's weight, then adds the bias
output = (inputs[0]*weights[0] +
		  inputs[1]*weights[1] +
		  inputs[2]*weights[2] + bias)

print(output)
