"""Benchmarks for slugify. Run: uv run pytest benchmarks --benchmark-only --no-cov

Coverage must stay off (--no-cov): tracing slows the code it measures. Only the plain
``benchmark(function, *args)`` call form is used, so pytest-codspeed can replace
pytest-benchmark later without changing this file.
"""

from pytest_benchmark.fixture import BenchmarkFixture

from python_template.text import slugify

SHORT = "Hello, World! Ñandú café"
LONG = ("Ñandú café Straße, the quick brown fox! " * 250)[:10_000]


def test_slugify_short(benchmark: BenchmarkFixture) -> None:
    assert benchmark(slugify, SHORT) == "hello-world-nandu-cafe"


def test_slugify_long(benchmark: BenchmarkFixture) -> None:
    result = benchmark(slugify, LONG)
    assert result.startswith("nandu-cafe-strasse-the-quick-brown-fox")
