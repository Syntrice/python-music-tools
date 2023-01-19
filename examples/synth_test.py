from matplotlib import pyplot as plt
from python_music_tools.synthesis.oscilator.oscilators import *

osc = iter(SquareOscilator(frequency=4, sample_rate=512))
osc1 = iter(SquareOscilator(frequency=4, sample_rate=512, threshhold=-0.5))
samples1 = [next(osc) for i in range(512)]
samples2 = [next(osc1) for i in range(512)]
x = range(512)

plt.plot(x, samples1, color='red')
plt.plot(x, samples2, color='blue')
plt.show()
