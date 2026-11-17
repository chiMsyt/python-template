# HANDOFF: python-template

**Next action (chiMsyt):** push branch `deps/uv-0.13` (needs Tim's OK), then close PR #1 as
superseded or merge it. Done = `ci` green on the branch's PR, run under uv 0.13.7, and PR #1
closed or merged.

**Still open after that:** the repository settings, all free on public repositories: a ruleset
on `main` requiring `ci-ok` with force pushes and deletion blocked; Dependabot alerts and
security updates; private vulnerability reporting; CodeQL default setup.

## uv 0.13 branch (`deps/uv-0.13`, local only, not pushed), 2026-11-18

- `uv_build` raised to `>=0.13.7,<0.14.0` (the same edit as PR #1) and `UV_VERSION` raised to
  `0.13.7` in `ci.yml`, `bench.yml` and `release.yml`. No other uv pins exist in the repo.
- Why 0.13.7 and not the newest 0.13.9: the repository's own Dependabot policy is a 7-day
  cooldown on new releases. 0.13.9 (2026-11-17) and 0.13.8 (2026-11-12) are inside it; 0.13.7
  (2026-11-03) is the newest outside it, and it is the floor Dependabot chose for `uv_build`.
  0.13.9 also changes how `uv.lock` writes environment markers, which could trip
  `UV_LOCKED=1`. Raise it once the cooldown has passed, through the next Dependabot PR.
- **Verified locally, with uv 0.12.6** (`UV_LOCKED=1`): every command the `ci` jobs run, plus
  the benchmarks, passes. `uv build` fetched the `uv_build` backend in range (0.13.9 at the
  time), so the 0.13 backend itself built and installed the wheel.
- **Not verified:** any command under uv 0.13.7 itself. The local uv was installed with
  winget, so `uv self update` refuses, and fetching uv 0.13.7 another way was not allowed. CI
  on the pushed branch is the first run under 0.13.7, including the preview `uv audit`.

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

- 2026-11-18: branch `deps/uv-0.13` (local): `uv_build` and the workflow `UV_VERSION`
  raised to 0.13.7 together, pairing Dependabot PR #1.
- 2026-11-18: published at github.com/chiMsyt/python-template (public, template
  repository); first `ci` run green.
- 2026-11-18: commit history rewritten to the owner's GitHub no-reply address before the
  first push; content unchanged (identical tree).
- 2026-11-18: changelog generation fixed for two or more releases (sections ran together);
  verified with markdownlint on single-release, multi-release and release-notes output.
- 2026-11-18: created. Package, CI, release and dependency automation, advisory benchmarks,
  security policy, issue forms.
