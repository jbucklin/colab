#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

filter_order = 16
command = 10
start_time = 0
end_time = 25
num_samples = 2500

time = np.linspace(start_time, end_time, num_samples)

input_history = [0]*filter_order
output_history = [0]*filter_order

aCoeffs = [0.16]*filter_order
bCoeffs = [0.01]*filter_order

#
# Filter function
def runFilter(value, index):
    index = (index + 1) % filter_order
    input_history[index] = value 

    output = sum([aCoeff*inp for aCoeff,inp in zip(aCoeffs, input_history)])
    output = output - sum([bCoeff*out for bCoeff,out in zip(bCoeffs, output_history)])
    output_history[index] = output
    return output


#
# Populate the time history and output values
#
Y = [0]*len(time)
error = [0]*len(time)
for i in range(len(time)):
    Y[i] = runFilter(command, i) 
    error[i] = command - Y[i]

#
# Plot the outputs
#
fig, ax = plt.subplots(figsize=(15,12))
ax.grid()
ax.plot(time, Y)
plt.show()

