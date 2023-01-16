import math
import numpy as np
import itertools

# basic sine wave generator
def get_sin_oscillator(freq, amp=1, phase=0, sample_rate=44100):
    
    # Convert phase in degrees to radians
    phase = np.deg2rad(phase % 360)
    
    # Calculate the increment between samples by dividing the period by the sample rate
    increment = 2 * np.pi * freq / sample_rate
    
    return (math.sin(phase + v) * amp for v in itertools.count(start=0, step=increment))