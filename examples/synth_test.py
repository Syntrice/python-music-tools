from matplotlib import pyplot as plt
from python_music_tools.synthesis.oscilator.oscilators import *
import numpy
freq = 440
sr = 44100
osc1 = iter(SineOscilator(freq, sample_rate=sr))
osc2 = iter(SquareOscilator(freq, sample_rate=sr))
osc3 = iter(SawtoothOscilator(freq, sample_rate=sr))
osc4 = iter(TriangleOscilator(freq, sample_rate=sr))
samples1 = [next(osc1) for i in range(sr)]
samples2 = [next(osc2) for i in range(sr)]
samples3 = [next(osc3) for i in range(sr)]
samples4 = [next(osc4) for i in range(sr)]
x = numpy.linspace(0, 1, sr)

plt.plot(x, samples1, color='red')
plt.plot(x, samples2, color='yellow')
plt.plot(x, samples3, color='green')
plt.plot(x, samples4, color='blue')
plt.show()
