#! /usr/bin/env python3
# -*- coding: utf-8

import click


@click.command()
@click.option("--count", default=1, help="number of greetings.")
@click.option("--name", prompt="Your name", help="the person to greet.")
def hello(count, name):
    """Simple program that greets name for a total of count times."""
    for _ in range(count):
        click.echo("Hello, %s!" % name)


if __name__ == "__main__":
    hello()
