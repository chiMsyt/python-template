#!/usr/bin/env bash
# Fails when portfolio.yml still carries another repository's identity: the usual result of
# creating a project from this template without updating the metadata.
set -euo pipefail

repository="${GITHUB_REPOSITORY:?GITHUB_REPOSITORY must be set to owner/name}"
expected="$(printf '%s' "${repository#*/}" | tr '[:upper:]' '[:lower:]')"
actual="$(sed -n -E "s/^id:[[:space:]]*[\"']?([a-z0-9-]+)[\"']?[[:space:]]*$/\1/p" portfolio.yml)"

if [ "$actual" != "$expected" ]; then
  echo "::error file=portfolio.yml::portfolio.yml id '${actual:-<missing>}' does not match repository '${expected}' — update portfolio.yml"
  exit 1
fi
echo "portfolio.yml id matches repository '${expected}'"
