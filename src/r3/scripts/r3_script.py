"""CLI script for the r3 package. This will be called on the command line"""

import click

from r3.r3 import hello_world


@click.command()
@click.option("--message", prompt="message", help="Type a message to say")
@click.version_option()
def r3_cli(message):
    """Example script. This function is referenced in setup.cfg"""
    click.echo(hello_world(message))
