"""datademo command line tool."""

import click
import dtool

from datademo import __version__

dataset_path_option = click.argument(
    'path',
    'Path to dataset directory',
    default=".",
    type=click.Path(exists=True))


@click.group()
@click.version_option(version=__version__)
def cli():
    pass


@cli.group()
def dataset():
    pass


@dataset.command()
@dataset_path_option
def identifiers(path):
    dataset = dtool.DataSet.from_path(path)
    click.secho(" ".join(dataset.identifiers))
