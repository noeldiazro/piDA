from abc import ABCMeta, abstractmethod
from .converter import Converter

class ADC(Converter):
    '''Abstract base class for classes that manage Analog/Digital converter operation'''
    __metaclass__ = ABCMeta

    def __init__(self, identifier, description, vref, bits, channels, data_link):
        Converter.__init__(self, identifier, description, vref, bits, channels, data_link)
        self._factor = self._vref / self._levels

    @abstractmethod
    def read_code(self, channel):
        pass

    def read(self, channel):
        return self.read_code(channel) * self._factor
