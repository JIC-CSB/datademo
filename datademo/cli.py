"""datademo command line tool."""

import os
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

project_path_option = click.argument(
    'path',
    'Path to project directory',
    default=".",
    type=click.Path(exists=True))


@click.group()
@click.version_option(version=__version__)
def cli():
    pass


#############################################################################
# datademo dataset
#############################################################################

@cli.group()
def dataset():
    pass


@dataset.command()
@dataset_path_option
def identifiers(path):
    dataset = dtool.DataSet.from_path(path)
    click.secho("\n".join(dataset.identifiers))


@dataset.command()
@dataset_path_option
def paths(path):
    dataset = dtool.DataSet.from_path(path)

    paths = [dataset.item_path_from_hash(identifier)
             for identifier in dataset.identifiers]

    click.secho('\n'.join(paths))


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


#############################################################################
# datademo project
#############################################################################

@cli.group()
def project():
    pass


@project.command()  # NOQA
@project_path_option
def summary(path):  # NOQA
    project = dtool.Project.from_path(path)

    num_datasets = 0
    num_files = 0
    tot_size = 0

    child_paths = [os.path.join(path, p) for p in os.listdir(path)]
    child_dirs = [d for d in child_paths if os.path.isdir(d)]

    for d in child_dirs:
        try:
            dataset = dtool.DataSet.from_path(d)
        except (dtool.DtoolTypeError, dtool.NotDtoolObject):
            continue

        file_list = dataset.manifest["file_list"]
        size = sum([f["size"] for f in file_list])

        num_datasets += 1
        num_files += len(file_list)
        tot_size += size

    json_lines = [
        "{",
        '  "Name": "{}",'.format(project.descriptive_metadata["project_name"]),
        '  "Number of datasets": {},'.format(num_datasets),
        '  "Number of files": {},'.format(num_files),
        '  "Total size": {}'.format(tot_size),
        "}",
    ]
    formatted_json = "\n".join(json_lines)
    colorful_json = pygments.highlight(
        formatted_json,
        pygments.lexers.JsonLexer(),
        pygments.formatters.TerminalFormatter())
    click.secho(colorful_json, nl=False)
