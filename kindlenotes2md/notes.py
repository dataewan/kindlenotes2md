import click
import os
import codecs
from pyquery import PyQuery
from .htmlparsing import get_author, get_title, get_notes
from .markdownoutput import md_output
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


def save_to_file(markdown: str, outfilename: str):
    if os.path.exists(outfilename):
        raise FileExistsError(f"{outfilename} already exists")

    with open(outfilename, "w") as f:
        f.write(markdown)


@click.command()
@click.argument("inputfilename")
@click.option("-o", "--outfilename", default=None)
def cli(inputfilename, outfilename):
    checkfile(inputfilename)
    contents = read_file(inputfilename)
    book_notes = parse_contents(contents)
    markdown = md_output(book=book_notes)
    if outfilename is None:
        print(markdown)
    else:
        save_to_file(markdown, outfilename)
