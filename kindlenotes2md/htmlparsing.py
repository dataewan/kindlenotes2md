import pyquery
from typing import List
from .dataclasses import Highlight, Section


def get_author(data: pyquery.PyQuery) -> str:
    return data("div.authors").text()


def get_title(data: pyquery.PyQuery) -> str:
    return data("div.bookTitle").text()


def get_notes(data: pyquery.PyQuery) -> List[Section]:
    results: List[Section] = []
    section = Section(title="", highlights=[])
    divs = data("div.noteText, div.noteHeading, div.sectionHeading")
    heading = ""
    text = ""
    for div in divs:
        _, className = div.items()[0]
        if className == "sectionHeading":
            if section.title != "":
                results.append(section)
            sectiontitle = div.text_content().strip()
            section = Section(title=sectiontitle, highlights=[])
        elif className == "noteHeading":
            heading = div.text_content().strip()
        elif className == "noteText":
            text = div.text_content().strip()
            section.highlights.append(Highlight(heading=heading, text=text))

    results.append(section)
    return results
