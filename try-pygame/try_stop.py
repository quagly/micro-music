#!/usr/bin/env python

# how to stop script when sound is over
# but don't exit if sound is playing

import numpy as np
import math
import pygame

from time import sleep


sRate = 44100 # samples per second
seconds_dur = 5 # number of seconds
nSamples = sRate * seconds_dur

# Create a numpy array of amplitude values via the second sine wave equation:
x = np.arange(nSamples)/float(sRate)
vals = np.sin(2.0*math.pi*220.0*x)

# So we can write to a file, the computed sine wave values in the range [-1, 1] are
# scaled to 16-bit values and converted to a string:
data = np.array(vals*32767, 'int16')

pygame.mixer.pre_init(frequency=sRate, size=-16, channels=1)
pygame.mixer.init()
sound = pygame.sndarray.make_sound(data)
# let pygame manage channels
channel = sound.play()
print(f'sound is {sound.get_length()} seconds')
while(channel.get_busy()):
      sleep(1)
