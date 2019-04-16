"""Contain class to GPIO pins on and off."""

import RPi.GPIO as GPIO


class Pin:
    """Implement GPIO pin handling class."""

    _on = GPIO.LOW
    _off = GPIO.HIGH

    def __init__(self, number: int = 17) -> None:
        """Construct instance, setup GPIO interface."""
        self.number = number

        # GPIO setup
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.number, GPIO.OUT)

    def on(self) -> None:
        """Turn pin on."""
        GPIO.output(self.number, self._on)

    def off(self) -> None:
        """Turn pin off."""
        GPIO.output(self.number, self._off)
        GPIO.cleanup()
