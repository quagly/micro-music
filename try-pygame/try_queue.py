#!/usr/bin/env python

# queues allow for adding sounds to a playing channel
# not sure if I need this

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

# initialize mixer
pygame.mixer.pre_init(frequency=sRate, size=-16, channels=1)
pygame.mixer.init()

# initialize channel
# channels are not required to be manually created as pygame can just handle it
# but I may want more control
# set number of channels
pygame.mixer.set_num_channels(1)
print(f'number of channels available is: {pygame.mixer.get_num_channels()}')
# channel numbering starts with zero
channel_zero = pygame.mixer.Channel(0)

# initialize sound
sound = pygame.sndarray.make_sound(data)
print(f'sound is {sound.get_length()} seconds')

# play sound on channel zero
# loop until done
channel_zero.play(sound)
while(channel_zero.get_busy()):
      sleep(1)

# queue a sound - it will play immediatly since nothing else is on the channel
channel_zero.queue(sound)

while(channel_zero.get_busy()):
      sleep(1)



