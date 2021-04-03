from click.testing import CliRunner

from kindlenotes2md import notes


def test_cli():
    runner = CliRunner()
    result = runner.invoke(notes.cli, "notexist.html")
    assert result.exit_code == 1
    result = runner.invoke(notes.cli, "tests/test_data.html")
    assert result.exit_code == 0


def test_readfile():
    notes.read_file("tests/test_data.html")
