from kindlenotes2md import htmlparsing
from pyquery import PyQuery

test_data = """
    <body>
        <div class="bodyContainer">
            <div class="notebookFor">
                Notebook Export
            </div>
            <div class="bookTitle">
                bookTitle
            </div>
            <div class="authors">
                Ewan Nicolson
            </div>
            <div class="citation">
                
            </div>
            <hr />
            <div class="sectionHeading">
    Introduction
</div><div class="noteHeading">
    Highlight(<span class="highlight_yellow">yellow</span>) - Page 2 · Location 187
</div>
<div class="noteText">
    Everyone has a plan
</div><div class="noteHeading">
    Highlight(<span class="highlight_yellow">yellow</span>) - Page 2 · Location 192
</div>
<div class="noteText">
    Until they get punched in the mouth
</div><div class="noteHeading">
    Highlight(<span class="highlight_yellow">yellow</span>) - Page 4 · Location 217
</div>
<div class="noteText">
    How to solve it
        </div>
    </body>
</html>
"""


data = PyQuery(test_data)


def test_author():
    result = htmlparsing.get_author(data)
    assert result == "Ewan Nicolson"


def test_title():
    result = htmlparsing.get_title(data)
    assert result == "bookTitle"


def test_notes():
    result = htmlparsing.get_notes(data)
    assert len(result) == 3
    assert result[0].text == "Everyone has a plan"
