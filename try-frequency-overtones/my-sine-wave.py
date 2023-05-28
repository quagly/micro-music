#!/usr/bin/env python

# example from https://github.com/joetechem/frequency_overtones_python
# this script simply generates a wav file
# to play a wav file use `afplay sine220.wav`

import numpy as np
import math
import wave

sRate = 44100
nSamples = sRate * 5

# Create a numpy array of amplitude values via the second sine wave equation:
x = np.arange(nSamples)/float(sRate)
vals = np.sin(2.0*math.pi*220.0*x)

# So we can write to a file, the computed sine wave values in the range [-1, 1] are
# scaled to 16-bit values and converted to a string:
data = np.array(vals*32767, 'int16').tostring()
file = wave.open('sine220.wav', 'wb')

# Set the parameters of the WAAV file:
file.setparams((1, 2, sRate, nSamples, 'NONE', 'uncompressed'))

# Write to the file using the parameters above:
file.writeframes(data)

# Close the file
file.close()
