import time
import pyaudio as pa
import numpy as np
from python_music_tools.synthesis import waves

# Parameters
sample_rate = 44100

# Initialize Pyaudio
p = pa.PyAudio()

wave = waves.sine_wave(1,440,1)

output_bytes = wave.tobytes()

# Open stream
stream = p.open(format=pa.paFloat32,
                channels=1,
                rate=sample_rate,
                output=True)

start_time = time.time()
stream.write(output_bytes)
print("Played sound for {:.2f} seconds".format(time.time() - start_time))

stream.stop_stream()
stream.close()

p.terminate()