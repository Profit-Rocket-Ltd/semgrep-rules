# Profit Rocket custom Semgrep rules

This directory holds **Profit-Rocket-specific** Semgrep rules that layer on top
of the upstream `frappe/semgrep-rules` ruleset.

## Why this directory exists

`Profit-Rocket-Ltd/semgrep-rules` is a fork of `frappe/semgrep-rules`. Upstream
rules cover Frappe correctness, security, code quality, translation and UX.
Project-specific rules — enforcing conventions from Profit Rocket's
[`STANDARD.md`](https://github.com/Profit-Rocket-Ltd/framework/blob/main/STANDARD.md)
and [`CLAUDE.md`](https://github.com/Profit-Rocket-Ltd/framework/blob/main/CLAUDE.md) —
live here so upstream syncs never collide with our additions.

## Layering contract

- **Never modify** `rules/*.yml` outside this directory. Treat upstream rules as
  read-only so `scripts/check_upstream_sync.sh` stays at category `SAFE`.
- New custom rules go under `rules/profit_rocket/<topic>.yml` with matching
  test fixtures `rules/profit_rocket/<topic>.py` (or `.js`).
- CI loads the full ruleset via `semgrep --config rules/`; the layered
  directory is picked up automatically.

## Running locally

From the framework repo root:

```bash
# Run upstream + custom rules against pr_app
PATH=".venv/bin:$PATH" PYTHONNOUSERSITE=1 \
  semgrep --config tools/semgrep-rules/rules apps/pr_app

# Validate rule test fixtures (target dir holds both rules and fixtures)
PATH=".venv/bin:$PATH" PYTHONNOUSERSITE=1 \
  semgrep --test tools/semgrep-rules/rules/profit_rocket
```

## Adding a rule

1. Write a `.yml` rule following [Semgrep rule syntax](https://semgrep.dev/docs/writing-rules/overview/).
2. Add a paired fixture file (`.py` or `.js`) with `# ruleid: <id>` markers on
   lines that should trigger and `# ok: <id>` markers on lines that should not.
3. Run `semgrep --test --config rules/profit_rocket` until it passes.
4. Open a PR — CI re-runs `--test` and a smoke scan against `pr_app`.

## Sync workflow

When upstream `frappe/semgrep-rules` advances, `scripts/check_upstream_sync.sh`
in the framework repo will flag it. Merge upstream into `develop` of this fork
with no edits outside `rules/profit_rocket/` — that keeps every sync a
fast-forward.
