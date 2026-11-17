# HANDOFF: python-template

**Next action (chiMsyt):** apply the repository settings, all free on public repositories:
a ruleset on `main` requiring `ci-ok` with force pushes and deletion blocked; Dependabot
alerts and security updates; private vulnerability reporting; CodeQL default setup. Then
merge Dependabot PR #1 (`uv-build` 0.13) together with raising `UV_VERSION` in the workflows
to a 0.13 release. Done = settings applied and PR #1 merged with CI green.

## State, 2026-11-18

**Verified locally** (Windows 11, Git Bash, `UV_LOCKED=1`): every command each CI job runs,
including the Python 3.12 leg; actionlint (with shellcheck) and zizmor at the auditor persona
report nothing; each checker was shown to fail on a deliberately broken input; the identity
guard's five cases; the release tag check and git-cliff notes in a tagged throwaway clone; the
benchmark gate (fails on a +35-70% regression, passes after revert).

**Verified on GitHub** (first push, 2026-11-18): `ci` green on all nine jobs, including the
Windows and macOS legs, each job 8–25 seconds; Dependabot opened PR #1 at once, and `ci` and
`bench` both ran green on it.

**Not verified yet:** `release.yml` end to end (needs a tag push, which publishes a real
release); build-provenance attestation; GitHub runner benchmark noise (run `bench.yml` five
times and apply the Management `bench_spread.py` analysis).

**Defaults the owner may want to change:** the seven-day acknowledgement promise in `SECURITY.md`;
the 90% coverage floor; the weekly Monday 01:30 UTC scheduled run.

## Failed approaches

- A bare `--cov` as the last pytest `addopts` entry swallows the first command-line path
  (`pytest benchmarks` ran the unit tests). Name the package: `--cov=python_template`.
- Case-folding before NFKD normalisation dropped letter-like symbols (U+2115 became nothing).
  Normalise first, then case-fold.
- `uv init` copies the git email into `pyproject.toml` `authors`. Write `pyproject.toml` by
  hand for public repos, or strip the field.

## Changelog

- 2026-11-18: published at github.com/chiMsyt/python-template (public, template
  repository); first `ci` run green.
- 2026-11-18: commit history rewritten to the owner's GitHub no-reply address before the
  first push; content unchanged (identical tree).
- 2026-11-18: changelog generation fixed for two or more releases (sections ran together);
  verified with markdownlint on single-release, multi-release and release-notes output.
- 2026-11-18: created. Package, CI, release and dependency automation, advisory benchmarks,
  security policy, issue forms.
