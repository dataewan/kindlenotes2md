from dataclasses import dataclass
from typing import List


@dataclass
class Highlight:
    heading: str
    text: str


@dataclass
class BookSummary:
    author: str
    title: str
    notes: List[Highlight]
