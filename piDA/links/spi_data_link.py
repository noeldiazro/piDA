from .data_link import DataLink
from spidev import SpiDev

class SPIDataLink(DataLink):
    '''Represents a link between a device an Raspberry Pi through Serial Peripheral Interface'''
    def __init__(self, bus, device, max_speed):
        self._bus = bus
        self._device = device
        DataLink.__init__(self, "SPI::" + str(bus) + "::" + str(device), "", max_speed)
        self._spi = SpiDev()

    @property
    def bus(self):
        return self._bus

    @property
    def device(self):
        return self._device

    def open(self):
        self._spi.open(self._bus, self._device)
        self._spi.max_speed_hz = self._max_speed

    def close(self):
        self._spi.close()

    def transfer(self, data):
        return self._spi.xfer2(data)
