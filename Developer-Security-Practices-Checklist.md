# Developer Security Practices — Practical Checklist for Developers

This is a compact, actionable checklist you can present in the workshop. It focuses on day-to-day practices developers can adopt to prevent common security issues and make automated/static scanners more effective.

## Short checklist (daily / per PR)
- [ ] Secrets: Do not hard-code secrets. Use environment variables or secret stores. Scan for accidentally committed secrets.
- [ ] Input validation: Validate or sanitize all external input; prefer allow-lists.
- [ ] Least privilege: Limit permissions for services, tokens, and processes.
- [ ] Dependency hygiene: Keep dependencies up-to-date and check for known CVEs.
- [ ] Use secure primitives: Prefer strong crypto (e.g., SHA-256 / HMAC) and avoid MD5/weak ciphers.
- [ ] Avoid shell injection: Do not build shell commands by concatenation; prefer safe API calls or argument lists.
- [ ] Error handling: Do not leak sensitive information in logs or error messages.
- [ ] Logging & monitoring: Log useful metadata (not secrets) and ensure alerts for critical events.
- [ ] Static checks: Run static security and linting checks locally before pushing.
- [ ] Review third-party code and 3rd-party services' security posture before integrating.

## PR checklist (what to tick before merging)
- [ ] Run the project's static analysis tools (Bandit, Snyk, Dependabot alerts, Flake8, ESLint).
- [ ] Confirm no secrets are present in the diff (use `git diff --staged` and a secret scanner).
- [ ] Check dependency changes for upgrades or new packages; run `safety`/`pip-audit` or equivalent.
- [ ] Confirm no high-severity Bandit or SCA findings are present; for accepted lower-severity findings, document rationale in the PR.
- [ ] Add unit tests for new behaviors or edge cases that affect security boundaries.
- [ ] Perform a short manual review of code that touches auth, crypto, input parsing, or subprocesses.

## Tool mapping (examples you can demonstrate)
- Secrets scanning: `git-secrets`, `truffleHog`, GitHub Secret Scanning.
- SAST / Security linting: `bandit` (Python), `semgrep` (multi-language), `brakeman` (Ruby), `spotbugs` (Java).
- Style / maintainability: `flake8`, `black`, `eslint`, `rubocop`.
- Dependency scanning: `pip-audit`, `safety`, `npm audit`, `dependabot`, `Snyk`.
- CI: GitHub Actions (integrate SAST + dependency scans), show how to upload scan reports as artifacts.

## Quick local commands (Python examples)

Create venv and install tools:

```powershell
python -m venv .venv
. .venv\Scripts\Activate.ps1
pip install bandit flake8 pip-audit
```

Run scans:

```powershell
python -m bandit -r demo_app
python -m flake8 demo_app
python -m pip_audit
```

Search staged changes for secrets (simple heuristic):

```powershell
git diff --cached | Select-String -Pattern "API_KEY|SECRET|PASSWORD|AWS_SECRET_ACCESS_KEY"
```

## How to handle findings (triage)
1. Classify by impact: RCE/data exposure/credential leak = high; weak style = low.
2. If secrets are found: rotate credentials immediately and remove from repo history.
3. For dependency CVEs: check if the vulnerable code path is reachable; upgrade or mitigate.
4. Document accepted risks in the PR and track remediation tasks if not fixed immediately.

## Workshop talking points (short)
- Developers should run scans locally and address high-severity items before opening PRs.
- Static tools reduce review time and catch common mistakes, but they don't replace manual review for logic/architecture issues.
- Make tooling frictionless: run checks automatically in CI and formatters on save.

---

Include this checklist in your workshop slides or handouts. Use the `demo_app` and `run_scans.ps1` in this repo to demonstrate concrete examples of several of these checks.
