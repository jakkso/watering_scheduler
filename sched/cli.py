"""Create CLI."""

import click

from sched.pin import Pin

PIN = Pin()
THIRTY_MIN = 1800


@click.group()
def group():
    """Watering Scheduler.

    Turning the pin on triggers a relay, which in turn opens a sprinkler valve, watering the garden.
    Currently, it is launched via a pair of contab entries: the first opens the valve, the second closes the valve.
    """


@click.command()
def on() -> None:
    """Turn pin on."""
    PIN.on()


@click.command()
def off() -> None:
    """Turn pin off."""
    PIN.off()


@click.command()
@click.option('--seconds', default=THIRTY_MIN)
def run(seconds: int) -> None:
    """Run program for 30 min."""
    PIN.run_for(seconds)


group.add_command(on)
group.add_command(off)
group.add_command(run)
