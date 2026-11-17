# HANDOFF: python-template

**Next action (Tim):** create `chiMsyt/python-template` on GitHub (public), push `main`,
tick **Template repository** in Settings, and watch the first `ci` run. Done = `ci-ok` green
with all eight test/lint/build/audit/config jobs green, and the repo labelled "Template".

## State, 2026-11-18

**Verified locally** (Windows 11, Git Bash, `UV_LOCKED=1`): every command each CI job runs,
including the Python 3.12 leg; actionlint (with shellcheck) and zizmor at the auditor persona
report nothing; each checker was shown to fail on a deliberately broken input; the identity
guard's five cases; the release tag check and git-cliff notes in a tagged throwaway clone; the
benchmark gate (fails on a +35-70% regression, passes after revert).

**Not verified yet** (needs GitHub): the workflows on GitHub runners, especially the Windows
and macOS legs; `release.yml` end to end (needs a tag push, creates a public release);
build-provenance attestation; Dependabot's first PRs; GitHub runner benchmark noise (run
`bench.yml` five times and apply the Management `bench_spread.py` analysis).

**Defaults Tim may want to change:** the seven-day acknowledgement promise in `SECURITY.md`;
the 90% coverage floor; the weekly Monday 01:30 UTC scheduled run.

## Failed approaches

- A bare `--cov` as the last pytest `addopts` entry swallows the first command-line path
  (`pytest benchmarks` ran the unit tests). Name the package: `--cov=python_template`.
- Case-folding before NFKD normalisation dropped letter-like symbols (U+2115 became nothing).
  Normalise first, then case-fold.
- `uv init` copies the git email into `pyproject.toml` `authors`. Write `pyproject.toml` by
  hand for public repos, or strip the field.

## Changelog

- 2026-11-18: created. Package, CI, release and dependency automation, advisory benchmarks,
  security policy, issue forms.
