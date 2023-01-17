from abc import ABC, abstractmethod

class Oscillator(ABC):
    
    # Constructor
    def __init__(self, frequency, phase, amplitude, sample_rate, wave_range):
        
        self._init_frequency, self._frequency = frequency
        self._init_phase, self._phase = phase
        self._init_amplitude, self._amplitude = amplitude
    
        self.sample_rate = sample_rate
        self.wave_range = wave_range
        
    # Initial Properties
    
    @property
    def init_frequency(self):
        return self._init_frequency
    
    @property
    def init_phase(self):
        return self._init_phase
    
    @property
    def init_amplitude(self):
        return self._init_amplitude
    
    # Frequency
    
    @property
    def frequency(self):
        return self._frequency
    
    @frequency.setter
    def frequency(self, value):
        self._frequency = value
        self._post_fequency_set()
    
    # Phase
    
    @property
    def phase(self):
        return self._phase 
    
    @phase.setter
    def phase(self, value):
        self._phase = value
        self._post_phase_set()
    
    # Amplitude
    
    @property
    def amplitude(self):
        return self._amplitude
    
    @amplitude.setter
    def amplitude(self, value):
        self._amplitude = value
        self._post_amplitude_set()
        
    # Functions that will run after a property is set
        
    def _post_frequency_set(self):
        pass
    
    def _post_phase_set(self):
        pass
    
    def _post_amplitude_set(self):
        pass
    
    # 
    
    @abstractmethod
    def initialize_osc(self):
        pass
    
    @staticmethod
    def squish_val(val, min_val=0, max_val=1):
        """
        function to squish a value between a min and max value
        """        
        return (((val + 1) / 2 ) * (max_val - min_val) ) + min_val 
    
    @abstractmethod
    def __next__(self):
        return None
    
    def __iter__(self):
        self.frequency = self._init_frequency
        self.phase  = self._init_phase
        self.amplitude = self._init_amplitude
        self.initialize_osc()
        return self