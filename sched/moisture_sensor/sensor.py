"""Contains Sensor class.

Sensor manages connection with board.


"""
import analogio
import board


class Sensor(analogio.AnalogIn):
    @property
    def voltage(self) -> float:
        """Return approx voltage."""
        return self.value / 65535 * 3.3
