"""datademo command line tool."""

import json

import click
import dtool
import pygments
import pygments.lexers
import pygments.formatters

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
def manifest(path):
    dataset = dtool.DataSet.from_path(path)
    formatted_json = json.dumps(dataset.manifest, indent=2)
    colorful_json = pygments.highlight(
        formatted_json,
        pygments.lexers.JsonLexer(),
        pygments.formatters.TerminalFormatter())
    click.secho(colorful_json, nl=False)


@dataset.command()
@dataset_path_option
def summary(path):
    dataset = dtool.DataSet.from_path(path)
    file_list = dataset.manifest["file_list"]
    total_size = sum([f["size"] for f in file_list])

    json_lines = [
        "{",
        '  "Name": "{}",'.format(dataset.name),
        '  "Creator": "{}",'.format(dataset.creator_username),
        '  "Number of files": {},'.format(len(file_list)),
        '  "Total size": {}'.format(total_size),
        "}",
    ]
    formatted_json = "\n".join(json_lines)
    colorful_json = pygments.highlight(
        formatted_json,
        pygments.lexers.JsonLexer(),
        pygments.formatters.TerminalFormatter())
    click.secho(colorful_json, nl=False)
