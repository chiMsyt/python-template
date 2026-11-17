# HANDOFF: python-template

**Next action (new session):** measure the GitHub runner benchmark noise floor. Run `bench.yml`
five times on the same `main` commit (`gh workflow run bench.yml --ref main`, one at a time),
download each run's `benchmark` artifact, then run Management's `scripts/bench_spread.py --stat
min run1.json … run5.json`. Done = five green `bench` runs on one SHA, and the per-benchmark
spread, the derived threshold and the run IDs recorded under "State" here and in Management's
benchmarking standard. Nothing is published: `workflow_dispatch` runs only upload artifacts.

**Still open after that:** `release.yml` end to end and build-provenance attestation. Both need
a tag push, which publishes a real release, so they wait for Tim's OK.

## Landing changes on `main`

`main` is protected by the ruleset "main protection": `ci-ok` must pass, force pushes and
deletion are blocked, nobody bypasses it.

1. Work on a branch, push it, open a PR with `gh pr create`.
2. Wait for `ci-ok` on the PR's head commit (`gh pr checks <n> --watch`). Never land red.
3. **Land by fast-forward only:** `git push origin <green-head-sha>:main`. Never use GitHub's
   merge button or `gh pr merge`: they make GitHub the committer and stamp the owner's
   personal name and email on the commit. A fast-forward keeps the commits exactly as pushed.
4. GitHub normally marks the PR merged on its own. If it does not, `gh pr close <n>
   --delete-branch`.
5. Sync: `git fetch --prune; git switch main; git reset --keep origin/main`, then delete the
   local branch.

Check afterwards: `git log origin/main --format='%ae %ce' | grep -v noreply` prints nothing.

## State, 2026-11-18

**Verified locally** (Windows 11, Git Bash, `UV_LOCKED=1`): every command each CI job runs,
including the Python 3.12 leg; actionlint (with shellcheck) and zizmor at the auditor persona
report nothing; each checker was shown to fail on a deliberately broken input; the identity
guard's five cases; the release tag check and git-cliff notes in a tagged throwaway clone; the
benchmark gate (fails on a +35-70% regression, passes after revert).

**Verified on GitHub:**

- First push: `ci` green on all nine jobs, including the Windows and macOS legs, each job 8–25
  seconds.
- uv and `uv_build` 0.13.7 (PR #2, commit `f7dbb23` on `main`): every `ci` job green under uv
  0.13.7, including the preview `uv audit` (run 44166945071).
- Repository settings, applied and read back through the API: ruleset "main protection"
  (active, requires `ci-ok`, blocks force pushes and deletion, no bypass); Dependabot alerts
  and security updates on; private vulnerability reporting on; CodeQL default setup
  (actions + python, first run green, 0 results); secret scanning and push protection on.

**Not verified yet:** `release.yml` end to end (needs a tag push, which publishes a real
release); build-provenance attestation; GitHub runner benchmark noise (the next action).

**Defaults the owner may want to change:** the seven-day acknowledgement promise in `SECURITY.md`;
the 90% coverage floor; the weekly Monday 01:30 UTC scheduled run; uv 0.13.7 rather than the
newest 0.13 (held back by the 7-day Dependabot cooldown; take the next Dependabot PR).

## Failed approaches

- A bare `--cov` as the last pytest `addopts` entry swallows the first command-line path
  (`pytest benchmarks` ran the unit tests). Name the package: `--cov=python_template`.
- Case-folding before NFKD normalisation dropped letter-like symbols (U+2115 became nothing).
  Normalise first, then case-fold.
- `uv init` copies the git email into `pyproject.toml` `authors`. Write `pyproject.toml` by
  hand for public repos, or strip the field.
- Landing a PR with GitHub's merge button or `gh pr merge` makes GitHub the committer with the
  owner's personal name and email. Land by fast-forward push instead (see above).
- `uv self update` refuses on a winget-installed uv, so a newer uv cannot be tried locally
  that way. CI on a pushed branch was the first run under uv 0.13.7.

## Changelog

- 2026-11-18: handoff rewritten after uv 0.13. Next action is the runner noise floor; landing
  rule (fast-forward only) added.
- 2026-11-18: repository settings applied and read back: ruleset "main protection",
  Dependabot alerts and security updates, private vulnerability reporting, CodeQL default
  setup, secret scanning with push protection.
- 2026-11-18: PR #2 landed as `f7dbb23`: `uv_build` raised to `>=0.13.7,<0.14.0` and
  `UV_VERSION` to 0.13.7 in `ci.yml`, `bench.yml` and `release.yml`, together. 0.13.7, not
  0.13.9, because the repository's 7-day Dependabot cooldown excluded 0.13.8 and 0.13.9, and
  0.13.9 also changes how `uv.lock` writes environment markers. Every `ci` job green under
  0.13.7 (run 44166945071). Dependabot PR #1 (the `uv_build` half alone) closed as
  superseded. Supersedes the local-only `deps/uv-0.13` branch entry below.
- 2026-11-18: branch `deps/uv-0.13` (local): `uv_build` and the workflow `UV_VERSION`
  raised to 0.13.7 together, pairing Dependabot PR #1. Verified locally under uv 0.12.6 only.
- 2026-11-18: published at github.com/chiMsyt/python-template (public, template
  repository); first `ci` run green.
- 2026-11-18: commit history rewritten to the owner's GitHub no-reply address before the
  first push; content unchanged (identical tree).
- 2026-11-18: changelog generation fixed for two or more releases (sections ran together);
  verified with markdownlint on single-release, multi-release and release-notes output.
- 2026-11-18: created. Package, CI, release and dependency automation, advisory benchmarks,
  security policy, issue forms.
