from abc import ABC, abstractmethod

class Oscilator(ABC):
    def __init__(self, frequency=440, phase=0, amplitude=1, sample_rate=44100, wave_range=(-1,1)):
    
        # properties that will not be changed
        self._sample_rate = sample_rate
        self._wave_range = wave_range
        self._init_frequency = frequency
        self._init_phase = phase
        self._init_amplitude = amplitude
        
        # properties that will be changed
        self._frequency = frequency
        self._phase = phase
        self._amplitude = amplitude
        
    # get initial properties
    @property
    def init_frequency(self):
        return self.init_frequency
    
    @property
    def init_phase(self):
        return self.init_phase
    
    @property
    def init_amplitude(self):
        return self.init_amplitude
    
    # modulatable properties
    @property
    def frequency(self):
        return self.frequency
    
    @frequency.setter
    def frequency(self, value):
        self.frequency = value
        self._post_frequency_set
        
    @property
    def amplitude(self):
        return self.amplitude
    
    @amplitude.setter
    def amplitude(self, value):
        self.amplitude = value
        self._post_amplitude_set
        
    @property
    def phase(self):
        return self.phase
    
    @phase.setter
    def phase(self, value):
        self.phase = value
        self._post_phase_set()
        
    def _post_frequency_set(self):
        pass
    
    def _post_amplitude_set(self):
        pass
    
    def _post_phase_set(self):
        pass
    
    @abstractmethod
    def _initialize_oscilator(self):
        pass
    
    @staticmethod
    def squish_val(val, min_val=0, max_val=1):
        return (((val + 1) / 2 ) * (max_val - min_val)) + min_val
            
    @abstractmethod
    def __next__(self):
        return None
    
    def __iter__(self):
        self.frequency = self._frequency
        self.phase = self._phase
        self.amplitude = self._amplitude
        self._initialize_oscilator()