import click
import os
import codecs
from dataclasses import dataclass
from pyquery import PyQuery
from . import htmlparsing


@dataclass
class BookSummary:
    author: str = ""
    title: str = ""


def checkfile(filename: str):
    """Perform some basic tests on the file to check it is what we expect. Fail fast"""
    if not (os.path.exists(filename)):
        raise FileNotFoundError


def read_file(filename: str) -> str:
    """Read file contents but don't do any parsing"""
    f = codecs.open(filename, "r")
    return f.read()


def parse_contents(contents: str) -> BookSummary:
    data = PyQuery(contents)
    author = htmlparsing.get_author(data)
    title = htmlparsing.get_title(data)
    bs = BookSummary(author=author, title=title)
    return bs


@click.command()
@click.argument("filename")
def cli(filename):
    checkfile(filename)
    contents = read_file(filename)
    parse_contents(contents)
