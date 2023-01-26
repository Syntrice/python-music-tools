from .oscilator_base import Oscilator
import math

class SineOscilator(Oscilator):
    def __next__(self):
        next_sample = math.sin(self._step + self._phase)
        self._step += self._step_size
        if self._wave_range != (-1, 1):
            next_sample = self.squish_val(next_sample, *self._wave_range)
        return next_sample * self._amplitude
    
class SquareOscilator(Oscilator):
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
    @Oscilator.phase.setter
    def phase(self, value):
        self._phase = ((value - 180 % 360) * math.pi / 180)
    
    def __next__(self):
        next_sample = ((self._step + self._phase) % (2 * math.pi)) / (math.pi) - 1
        self._step += self._step_size
        if self._wave_range != (-1, 1):
            next_sample = self.squish_val(next_sample, *self._wave_range)
        return next_sample * self._amplitude
    
class TriangleOscilator(Oscilator):
    @Oscilator.phase.setter
    def phase(self, value):
        self._phase = ((value - 90 % 360) * math.pi / 180)
    
    def __next__(self):
        next_sample = 4 * abs((self._step + self._phase) % (2 * math.pi) / (2 * math.pi) - 0.5) - 1
        self._step += self._step_size
        if self._wave_range != (-1, 1):
            next_sample = self.squish_val(next_sample, *self._wave_range)
        return next_sample * self._amplitude
    
    