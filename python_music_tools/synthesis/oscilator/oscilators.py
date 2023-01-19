from .oscilator_base import Oscilator
import math

class SineOscilator(Oscilator):
    @Oscilator.frequency.setter
    def frequency(self, value):
        self._frequency = value
        self._step_size = (2 * math.pi * self._frequency) / self._sample_rate
    
    @Oscilator.phase.setter
    def phase(self, value):
        self._phase = (value % 360) * math.pi / 180
    
    def __next__(self):
        next_sample = math.sin(self._step + self._phase)
        self._step += self._step_size
        if self._wave_range is not (-1, 1):
            next_sample = self.squish_val(next_sample, *self._wave_range)
        return next_sample * self._amplitude
    
class SquareOscilator(SineOscilator):
    def __init__(self, frequency=440, phase=0, amplitude=1, sample_rate=44100, wave_range=(-1, 1), threshhold=0):
        super().__init__(frequency, phase, amplitude, sample_rate, wave_range)
        self.threshhold = threshhold
        
    def __next__(self):
        next_sample = math.sin(self._step + self._phase)
        self._step += self._step_size
        if next_sample < self.threshhold:
            next_sample = self._wave_range[0]
        else:
            next_sample = self._wave_range[1]
        return next_sample * self._amplitude
    
class SawtoothOscilator(Oscilator):
    pass
    
class TriangleOscilator(Oscilator):
    pass