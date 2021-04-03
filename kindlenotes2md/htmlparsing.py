import pyquery
from typing import List
from .dataclasses import Highlight


def get_author(data: pyquery.PyQuery) -> str:
    return data("div.authors").text()


def get_title(data: pyquery.PyQuery) -> str:
    return data("div.bookTitle").text()


def get_notes(data: pyquery.PyQuery) -> List[Highlight]:
    headings = get_headings(data)
    texts = get_texts(data)
    return [
        Highlight(heading=heading, text=text) for heading, text in zip(headings, texts)
    ]


def get_headings(data: pyquery.PyQuery) -> List[str]:
    headings = data("div.noteHeading")
    return [i.text_content().strip() for i in headings]


def get_texts(data: pyquery.PyQuery) -> List[str]:
    headings = data("div.noteText")
    return [i.text_content().strip() for i in headings]
