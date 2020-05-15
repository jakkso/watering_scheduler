"""Contain class to turn GPIO pins on and off."""
import time

try:
    import RPi.GPIO as GPIO
except ImportError:
    pass

from sched.logger import logger
from sched.config import Config


def get_state() -> int:
    """Return pin's state."""
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    return GPIO.input(Config.PIN_NUMBER)


class Pin:
    def __init__(self, number: int = 17):
        self.number = number
        self.logger = logger()
        # GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def clean_up(self) -> None:
        GPIO.cleanup()

    def toggle(self) -> bool:
        """Toggle pin."""
        with InputPin():
            state = GPIO.input(self.number)
        with OutputPin() as pin:
            if state:
                pin.on()
            else:
                pin.off()
        return not state


class _Pin:
    """Implement GPIO pin handling parent class."""

    _on = GPIO.LOW
    _off = GPIO.HIGH

    def __init__(self, number: int = 17) -> None:
        """Construct instance."""
        self.number = number
        self.logger = logger()
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class InputPin(_Pin):
    """Provide interface to read pin state."""

    def __init__(self, number: int = 17):
        """Construct object, input mode only."""
        super().__init__(number)
        GPIO.setup(self.number, GPIO.IN)

    def __exit__(self, exc_type, exc_val, exc_tb):
        GPIO.cleanup()

    @property
    def state(self) -> int:
        """Return relay state."""
        return GPIO.input(self.number)


class OutputPin(_Pin):
    def __init__(self, number: int = 17) -> None:
        """Construct instance, output mode only.

        :param number: BCM pin number
        """
        super().__init__(number)
        GPIO.setup(self.number, GPIO.OUT)

    def on(self) -> None:
        """Turn pin on."""
        GPIO.output(self.number, self._on)
        self.logger.info("Valve opened.")

    def off(self) -> None:
        """Turn pin off."""
        GPIO.output(self.number, self._off)
        GPIO.cleanup()
        self.logger.info("Valve closed.")

    def run_for(self, seconds: int) -> None:
        """Open valve, sleep for `seconds`, close valve.

        Prior to now, I've started the program via a pair of cron jobs, one to
        open the valve, another to close it.  However, cron jobs can fail.
        If the first job fails, it's no big deal: the water doesn't go on.  If the
        second job fails, the valve never closes, and the water keeps running forever.
        """
        self.on()
        time.sleep(seconds)
        self.off()
