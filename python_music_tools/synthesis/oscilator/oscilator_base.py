from abc import ABC, abstractmethod
import math

class Oscilator(ABC):
    
    def __init__(self, frequency=440, phase=0, amplitude=1, sample_rate=44100, wave_range=(-1, 1)):
        
        self._init_frequency = frequency
        self._init_phase = phase
        self._init_amplitude = amplitude
        self._sample_rate = sample_rate
        self._wave_range = wave_range
        self.initialize()
        
    @property
    def init_frequency(self):
        return self._init_frequency
    
    @property
    def init_phase(self):
        return self._init_phase
    
    @property
    def init_amplitude(self):
        return self._init_amplitude
        
    @property
    def frequency(self):
        return self._frequency
    
    @frequency.setter
    def frequency(self, value):
        self._frequency = value
        self._step_size = (2 * math.pi * self._frequency) / self._sample_rate
        
    @property
    def phase(self):    
        return self._phase

    @phase.setter
    def phase(self, value):
        self._phase = (value % 360) * math.pi / 180
    
    @property
    def amplitude(self):
        return self._amplitude
        
    @amplitude.setter
    def amplitude(self, value):
        self._amplitude = value
        
    def initialize(self):
        self._step = 0 # iterator
        self.frequency = self.init_frequency
        self.phase = self.init_phase
        self.amplitude = self.init_amplitude
        
    @abstractmethod
    def __next__(self):
        return None
        
    def __iter__(self):
        self.initialize()
        return self
    
    @staticmethod
    def squish_val(val, min_val=0, max_val=1):
        """
        function to squish a value between a min and max value
        """        
        return (((val + 1) / 2 ) * (max_val - min_val) ) + min_val
    