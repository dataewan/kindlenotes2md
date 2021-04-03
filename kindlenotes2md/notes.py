import click
import os
import codecs
from pyquery import PyQuery
from .htmlparsing import get_author, get_title, get_notes
from .dataclasses import BookSummary


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
    author = get_author(data)
    title = get_title(data)
    notes = get_notes(data)
    bs = BookSummary(author=author, title=title, notes=notes)
    return bs


@click.command()
@click.argument("filename")
def cli(filename):
    checkfile(filename)
    contents = read_file(filename)
    book_notes = parse_contents(contents)
    print(book_notes)
