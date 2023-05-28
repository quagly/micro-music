#!/usr/bin/env python

import argparse
import logging
import matplotlib.pyplot as plt
import numpy as np
import os
import pygame
import random
import statistics
import time
import wave

from collections import deque


gShowPlot = False

# implementation of Karplus-Strong Algorithm
# https\://github.com/joetechem/frequency_overtones_python\#slice-1---karplus-strong-algorithm

# generate note of given frequency


def generateNote(freq):
    # sample rate, 44100 is compact disk standard
    nSamples = 44100
    sampleRate = 44100
    # factor to reduce amplitude for each sample.
    # so that volume reduces as the string is dampend
    attenuation = 0.995
    # the length of the ring buffer is number of samples divided by frequency
    # for example if frequncy is 441 Hz and samples are 44100 then 44100/441 = 100 samples
    # seems like a lower frequncy needs more samples because the wavelength is longer
    N = int(sampleRate/freq)
    # initialize ring buffer
    # with random numbers [-0.5, 0.5] to simulate the random displacement of the string as it vibrates
    # we will pull from the front and add to the end of the ring buffer as we move through time
    buf = deque([random.random() - 0.5 for i in range(N)])
    # init sample buffer with zeros
    samples = np.array([0]*nSamples, 'float32')
    for i in range(nSamples):
        # get the first element of the buffer
        samples[i] = buf[0]
        # average the first two elements of the buffer, redude amplitude by attenuation, and append buffer
        avg = attenuation*statistics.mean([buf[0], buf[1]])
        buf.append(avg)
        # remove the first element of the buffer
        buf.popleft()
        # plot of flag set
        if gShowPlot:
            raise ValueError(f'graphical plotting not implmented but gShowPlot={gShowPlot}')
            # if i % 1000 == 0:
            # this fails as axline is not set
            # I would need to learn matplotlib to debug
            # maybe use audacity on the wav files in the meantime
            # axline.set_ydata(buf)
            # plt.draw()

    # samples to 16-bit
    # 16-bit is compact disk standard
    # max value is 32767 for 16-bit
    samples = np.array(samples * 32767, 'int16')
    # why a string? because we are writing to a wav file
    # seems like the writer should handle this
    return samples.tostring()


def writeWAVE(fname, data):
    '''write out WAVE file'''
    # open file
    # can I use a context manager with wave?
    # write binary file
    file = wave.open(fname, 'wb')
    # WAV file parameters
    nChannels = 1
    sampleWidth = 2
    frameRate = 44100
    nFrames = 44100
    # set parameters
    file.setparams((nChannels, sampleWidth, frameRate, nFrames,
                    'NONE', 'noncompressed'))
    file.writeframes(data)
    file.close()


# play a wav file
class NotePlayer:
    # constructor
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 1, 2048)
        pygame.init()
        # dictionary of notes
        self.notes = {}

    # add a note

    def add(self, fileName):
        self.notes[fileName] = pygame.mixer.Sound(fileName)

    # play a note

    def play(self, fileName):
        try:
            self.notes[fileName].play()
        except:
            print(fileName + ' not found!')

    def playRandom(self):
        """play a random note"""
        index = random.randint(0, len(self.notes)-1)
        note = list(self.notes.values())[index]
        note.play()


def main():
    # declare global var so that it can be changed
    global gShowPlot

    # pmNotes is apparently a dictionary of names and frequencies
    # it did not exist in the sample code
    # lets try
    pmNotes = {
        "A4": 440,
        "A3": 220
    }

    parser = argparse.ArgumentParser(description="Generating sounds with Karplus String Algorithm.")
    # add arguments
    parser.add_argument('--display', action='store_true', required=False)
    parser.add_argument('--play', action='store_true', required=False)
    parser.add_argument('--piano', action='store_true', required=False)
    args = parser.parse_args()

    # show plot if flag set
    if args.display:
        gShowPlot = True
        plt.ion()

    # create note player
    nplayer = NotePlayer()

    print('creating notes...')
    for name, freq in list(pmNotes.items()):
        fileName = name + '.wav'
        if not os.path.exists(fileName) or args.display:
            data = generateNote(freq)
            print('creating ' + fileName + '...')
            writeWAVE(fileName, data)
        else:
            print('fileName already created. skipping...')
        # add note to player
        nplayer.add(name + '.wav')
        # play note if display flag set
        if args.display:
            nplayer.play(name + '.wav')
            time.sleep(0.5)
    # play a random tune
    if args.play:
        while True:
            try:
                nplayer.playRandom()
                # rest - 1 to 8 beats
                rest = np.random.choice([1, 2, 4, 8], 1,
                                        p=[0.15, 0.7, 0.1, 0.05])
                time.sleep(0.25*rest[0])
            except KeyboardInterrupt:
                exit()


if __name__ == '__main__':
    try:
        logging.basicConfig(format="%(asctime)s %(lineno)d %(message)s",
                            level=logging.INFO)
        log = logging.getLogger(__file__)
        main()
    except Exception:
        log.exception("FAILED: script {0})".format(__file__))
        # I am logging to the console so no need to raise
        # except for exit code, so just provide exit code
        # raise
        exit(1)
