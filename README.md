# kindlenotes2md

Command line utility to convert your Kindle highlights from html to markdown.


## Installation

```
pip install kindlenotes2md
```

## Usage

From the Kindle app, you have the option to export the highlights that you've made in the book.
The easiest way to get access to these are to email them to yourself.
These exported highlights are in html format, so are a bit tricky to use in other tools.

Run this tool with the `.html` file as a command line argument.

```
kindlenotes2md INPUTFILENAME
```

Here's the documentation for the tool you get by running `--help`.

```
Usage: kindlenotes2md [OPTIONS] INPUTFILENAME

Options:
  -o, --outfilename TEXT
  --help                  Show this message and exit.
```

You have the option to specify a filename with `-o` or `--outfilename`.
This will write the markdown output to file, rather than stdout.
