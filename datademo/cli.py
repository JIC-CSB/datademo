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


@dataset.command()
@dataset_path_option
def summary(path):
    dataset = dtool.DataSet.from_path(path)
    file_list = dataset.manifest["file_list"]
    total_size = sum([f["size"] for f in file_list])
    click.secho("Name: {}".format(dataset.name))
    click.secho("Creator: {}".format(dataset.creator_username))
    click.secho("Number of files: {}".format(len(file_list)))
    click.secho("Total size: {}".format(total_size))
