"""Contain class to turn GPIO pins on and off."""
import time

import RPi.GPIO as GPIO

from sched.logger import logger


class Pin:
    """Implement GPIO pin handling class."""

    _on = GPIO.LOW
    _off = GPIO.HIGH

    def __init__(self, number: int = 17) -> None:
        """Construct instance, setup GPIO interface.

        :param number: BCM pin number
        """
        self.number = number
        self.logger = logger()

        # GPIO setup
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
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

    def toggle(self) -> bool:
        """Toggle relay state, return current state."""
        state = self.state
        if state:
            self.off()
        else:
            self.on()
        return not state

    @property
    def state(self) -> int:
        """Return relay state."""
        return GPIO.input(self.number)
