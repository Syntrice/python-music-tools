import numpy as np
 
def sine_wave(amplitude, frequency, duration, sample_rate=44100):
    
    # Calculate the total number of samples for the given sample rate and duration
    num_samples = int(duration * sample_rate)
    
    # Create an array with the corresponding time values of each sample
    t = np.linspace(0, duration, num_samples)
    
    # Calculate the displacement values for each individual sample time. (2 * np.pi * t gives one cycle per second, multiple by frequency to get desired cycles per second)
    d = amplitude * np.sin(2 * np.pi * t * frequency)
    
    return d.astype(np.float32)