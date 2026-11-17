"""Command-line entry point. Example code: replace with the project's own commands."""

import argparse
from collections.abc import Sequence
from importlib.metadata import version

from python_template.text import slugify


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python-template")
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {version('python-template')}"
    )
    commands = parser.add_subparsers(dest="command", required=True)
    slug_command = commands.add_parser("slugify", help="print TEXT as a URL slug")
    slug_command.add_argument("text")
    slug_command.add_argument("--max-length", type=int, default=None)
    args = parser.parse_args(argv)
    try:
        print(slugify(args.text, max_length=args.max_length))
    except ValueError as error:
        parser.error(str(error))
    return 0
