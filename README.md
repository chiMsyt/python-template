<div align="center">

# python-template

**Start a Python project with the tedious parts already done, and already passing.**

[![ci](https://github.com/chiMsyt/python-template/actions/workflows/ci.yml/badge.svg)](https://github.com/chiMsyt/python-template/actions/workflows/ci.yml)

</div>

A GitHub template repository. A project created from it begins with packaging, linting,
type checking, tests with a coverage floor, a dependency audit, workflow security checks,
benchmarks and tag-driven releases already configured, so its first commit is green instead
of its tenth.

The package inside, a small `slugify` function and CLI, exists only so every check has real
code to work on. A new project replaces it.

## What a new project gets

- **Checks that agree everywhere.** Every tool version is locked in `uv.lock`, so a check
  that passes on your machine passes in CI, and the other way round.
- **One required check.** Branch protection needs only `ci-ok`, which fails if any job
  fails or is skipped.
- **Tests where users are.** Linux on the oldest and newest supported Python, plus
  Windows and macOS.
- **Supply-chain care by default.** Actions are pinned to commit SHAs, dependencies are
  checked against known vulnerabilities on every run and weekly, and Dependabot proposes
  updates only after a 7-day cooldown.
- **Releases from a tag.** Push `v1.2.3` and CI tests, builds, verifies, attests and
  publishes the release, with notes written from the commit history.
- **Benchmarks that mean something.** Regressions are caught locally against a saved
  baseline, with a threshold derived from measured noise; CI benchmark runs are advisory.
- **Metadata for the portfolio site.** `portfolio.yml` describes the project; CI validates
  it and checks it names this repository.

## Why it is built this way

| Decision | Reason |
| --- | --- |
| Copied into each project, not shared at run time | Each repository stays self-contained and keeps working if this one changes. |
| mypy, not ty | ty is still in beta (0.0.x). A blocking check should be stable; revisit at ty 1.0. |
| Benchmarks gate on the minimum time | Measured on a shared desktop, the minimum was five times steadier than the median. |
| Benchmarks never block CI | Shared CI runners are too noisy to judge a change by a single timing. |
| No license file | The license is chosen per project. |

## Use this template

1. On GitHub, **Use this template → Create a new repository**. Use a lowercase-kebab name.
2. Rename the package: move `src/python_template/` to `src/<your_package>/`, then replace
   `python_template` and `python-template` across the repository (one project-wide search
   and replace covers `pyproject.toml`, tests, benchmarks, issue forms and `portfolio.yml`).
3. Edit `portfolio.yml`. Its `id` must equal the repository name; CI fails until it does.
4. Replace the example code, tests and benchmarks with the project's own.
5. Rewrite this README and `HANDOFF.md` for the new project, and reset the changelog:
   `uv run --group ci git-cliff -o CHANGELOG.md`.
6. Choose a license: add `LICENSE` and `license = "<SPDX id>"` to `pyproject.toml`.
7. In the repository settings: a branch ruleset on `main` requiring the `ci-ok` check;
   Dependabot alerts and security updates; private vulnerability reporting; CodeQL default
   setup (public repositories).
8. Private repository? Delete the `windows-latest` and `macos-latest` rows from the test
   matrix in `.github/workflows/ci.yml`: they draw on the Actions allowance at higher rates.

## Develop

Requires [uv](https://docs.astral.sh/uv/). It installs the right Python by itself.

```console
uv sync
uv run pytest
```

| Check | Command | Blocks a merge |
| --- | --- | --- |
| Lockfile matches `pyproject.toml` | `uv lock --check` | yes |
| Formatting | `uv run ruff format --check .` (fix: `uv run ruff format .`) | yes |
| Lint | `uv run ruff check .` (fix: add `--fix`) | yes |
| Types | `uv run mypy` | yes |
| Tests, branch coverage of at least 90% | `uv run pytest` | yes |
| Known vulnerabilities | `uv audit --preview-features audit-command` | yes |
| Build and install | `uv build`, then `uv run --isolated --no-project --with dist/*.whl python-template --version` | yes |
| Workflows | `uv run --group ci actionlint` and `uv run --group ci zizmor --offline .github/workflows` | yes |
| Benchmarks | `uv run pytest benchmarks --benchmark-only --no-cov` | no |

To check a change for a speed regression, save a baseline first, then compare:

```console
uv run pytest benchmarks --benchmark-only --no-cov --benchmark-save=baseline
# ...make the change...
uv run pytest benchmarks --benchmark-only --no-cov --benchmark-compare --benchmark-compare-fail=min:10%
```

## Release

```console
uv version --bump minor
uv run --group ci git-cliff --tag "v$(uv version --short)" -o CHANGELOG.md
git commit -am "chore(release): v$(uv version --short)"
git tag "v$(uv version --short)"
git push origin main "v$(uv version --short)"
```

Pushing the tag runs `release.yml`, which refuses to publish if the tag and the package
version disagree.

## Stack

Python 3.12+ · uv · ruff · mypy · pytest with pytest-cov and pytest-benchmark ·
GitHub Actions · Dependabot · git-cliff · actionlint · zizmor

## Security

See [SECURITY.md](SECURITY.md).
