from .dataclasses import BookSummary, Section, Highlight


def md_title(book: BookSummary) -> str:
    return f"# {book.title}\n\n"


def md_author(book: BookSummary) -> str:
    return f"## {book.author}\n\n---\n\n"


def md_highlight(highlight: Highlight) -> str:
    return f"{highlight.heading}\n: {highlight.text}\n\n"


def md_section(section: Section) -> str:
    output = f"### {section.title}\n\n"

    for highlight in section.highlights:
        output = output + md_highlight(highlight)

    return output


def md_output(book: BookSummary) -> str:
    markdown = ""
    markdown = markdown + md_title(book)
    markdown = markdown + md_author(book)

    for section in book.notes:

        markdown = markdown + md_section(section)

    return markdown
