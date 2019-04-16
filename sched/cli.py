"""Create CLI."""

import click

from sched.pin import Pin

PIN = Pin()


@click.group()
def group():
    """Group CLI commands."""
    pass


@click.command()
def on() -> None:
    """Turn pin on."""
    PIN.on()


@click.command()
def off() -> None:
    """Turn pin off."""
    PIN.off()


group.add_command(on)
group.add_command(off)
