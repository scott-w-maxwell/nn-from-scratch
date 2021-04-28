inputs = [1, 2, 3]
weights = [0.2, 0.8, -0.5]
bias = 2

# Single Neuron sums each input multiplied by that input's weight, then adds the bias
output = (inputs[0]*weights[0] +
		  inputs[1]*weights[1] +
		  inputs[2]*weights[2] + bias)

print("Output for single neuron 3 inputs", output)


# Single Neuron with 4 inputs

inputs = [1.0, 2.0, 3.0, 2.5]
weights = [0.2, 0.8, -0.5, 1.0]
bias = 2.0

output = (inputs[0]*weights[0] +
		  inputs[1]*weights[1] +
		  inputs[2]*weights[2] +
		  inputs[3]*weights[3] + bias)

print("Output for single neuron 4 inputs", output)

# Three neuron layer with 4 inputs
inputs = [1, 2, 3, 2.5]
weights1 = [0.2, 0.8, -0.5, 1]
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]
bias1 = 2
bias2 = 3
bias3 = 0.5


			 # Neuron 1:
outputs = [	 inputs[0]*weights1[0] +
			 inputs[1]*weights1[1] +
			 inputs[2]*weights1[2] +
			 inputs[3]*weights1[3] + bias1,
			 # Neuron 2:
			 inputs[0]*weights2[0] +
			 inputs[1]*weights2[1] +
			 inputs[2]*weights2[2] +
			 inputs[3]*weights2[3] + bias2,
			 # Neuron 3:
			 inputs[0]*weights3[0] +
			 inputs[1]*weights3[1] +
			 inputs[2]*weights3[2] +
			 inputs[3]*weights3[3] + bias3]

print("Output for 3 layer neuron with 4 inputs", outputs)


# compacted code (Same as above):

inputs = [1, 2, 3, 2.5]
weights = [[0.2, 0.8, -0.5, 1],
 		   [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]
biases = [2, 3, 0.5]
# Output of current layer
layer_outputs = []
# For each neuron
for neuron_weights, neuron_bias in zip(weights, biases):
	# Zeroed output of given neuron
	neuron_output = 0
	# For each input and weight to the neuron
	for n_input, weight in zip(inputs, neuron_weights):
		# Multiply this input by associated weight
		# and add to the neuron's output variable
		neuron_output += n_input*weight
	# Add bias
	neuron_output += neuron_bias
	# Put neuron's result to the layer's output list
	layer_outputs.append(neuron_output)
print("Output for same example but scalable code",layer_outputs)

