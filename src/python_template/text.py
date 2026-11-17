"""Text helpers. Example code: replace with the project's own modules."""

import re
import unicodedata

_NON_ALNUM_RUN = re.compile(r"[^a-z0-9]+")


def slugify(text: str, *, max_length: int | None = None) -> str:
    """Return ``text`` as a lowercase ASCII slug: words joined by single hyphens.

    Text is decomposed (NFKD) before case-folding, so letter-like symbols (U+2115, the
    double-struck N) reduce to a letter before they are lowered. Case-folding turns
    "Straße" into "strasse", and accents fall away ("café" -> "cafe"). Characters with no
    ASCII form are dropped. With ``max_length`` the slug holds at most that many characters
    and never ends in a hyphen.
    """
    if max_length is not None and max_length < 1:
        msg = "max_length must be a positive integer"
        raise ValueError(msg)
    ascii_text = unicodedata.normalize("NFKD", text).casefold().encode("ascii", "ignore")
    slug = _NON_ALNUM_RUN.sub("-", ascii_text.decode("ascii")).strip("-")
    if max_length is not None:
        slug = slug[:max_length].rstrip("-")
    return slug
