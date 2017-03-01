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

    click.secho("Name: ", nl=False)
    click.secho(dataset.name, fg="green")

    click.secho("Creator: ", nl=False)
    click.secho(dataset.creator_username, fg="green")

    click.secho("Number of files: ", nl=False)
    click.secho(str(len(file_list)), fg="green")

    click.secho("Total size: ", nl=False)
    click.secho(str(total_size), fg="green")
