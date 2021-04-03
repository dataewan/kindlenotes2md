import pyquery


def get_author(data: pyquery.PyQuery) -> str:
    return data("div.authors").text()


def get_title(data: pyquery.PyQuery) -> str:
    return data("div.bookTitle").text()
