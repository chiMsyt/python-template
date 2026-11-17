from importlib.metadata import version

import pytest

from python_template.cli import main


def test_slugify_command_prints_the_slug(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["slugify", "Hi There"]) == 0
    assert capsys.readouterr().out == "hi-there\n"


def test_version_flag_prints_the_installed_version(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as exit_info:
        main(["--version"])
    assert exit_info.value.code == 0
    assert capsys.readouterr().out.strip() == f"python-template {version('python-template')}"


def test_invalid_max_length_is_a_usage_error(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as exit_info:
        main(["slugify", "x", "--max-length", "0"])
    assert exit_info.value.code == 2
    assert "max_length must be a positive integer" in capsys.readouterr().err
