import pytest

from python_template.text import slugify


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hello, World!", "hello-world"),
        ("  Ñandú café  ", "nandu-cafe"),
        ("Straße", "strasse"),
        ("\N{DOUBLE-STRUCK CAPITAL N}atural \N{DOUBLE-STRUCK CAPITAL H}istory", "natural-history"),
        ("a---b__c", "a-b-c"),
        ("", ""),
        ("!!!", ""),
    ],
)
def test_slugify_makes_lowercase_ascii_hyphenated_slugs(text: str, expected: str) -> None:
    assert slugify(text) == expected


def test_max_length_caps_the_slug() -> None:
    assert slugify("hello world foo", max_length=11) == "hello-world"


def test_max_length_never_leaves_a_trailing_hyphen() -> None:
    assert slugify("hello world", max_length=6) == "hello"


@pytest.mark.parametrize("max_length", [0, -1])
def test_max_length_below_one_is_rejected(max_length: int) -> None:
    with pytest.raises(ValueError, match="max_length must be a positive integer"):
        slugify("hello", max_length=max_length)
