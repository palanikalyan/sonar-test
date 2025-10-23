# Developer Checklist for Static Analysis, Code Review, and Automated Scans

This checklist is designed for a short workshop/demo showing how to integrate static analysis into the developer workflow, triage results, and improve code quality. It includes a tiny demo app and scripts to run scans locally and in CI.

## Goals
- Show common findings (security, style, complexity).
- Demonstrate running tools locally and in CI.
- Teach triage steps and how to prioritize fixes.

## Materials in this repo
- `demo_app/` - tiny Python app with intentional issues for demo.
- `run_scans.ps1` - PowerShell script to install deps and run Bandit and Flake8 locally.
- `.github/workflows/static-analysis.yml` - GitHub Actions workflow to run scans on push/PR.
- `Developer-Checklist-for-Static-Analysis-Code-Review-Automated-Scans.md` - this file.
- `README.md` - quick start for the demo.

## Checklist (for the workshop/demo)

Pre-demo
- [ ] Clone the repository to your machine.
- [ ] Open the repo in VS Code.
- [ ] Install Python 3.8+ and pip.

Local demo
- [ ] Run `run_scans.ps1` from PowerShell to install tool deps and run scans.
- [ ] Show Bandit findings (security issues).
- [ ] Show Flake8 findings (style/complexity).

CI demo
- [ ] Push a change or open a PR to trigger `static-analysis` workflow.
- [ ] Show workflow run, annotations, and artifacts.

Triaging and fixing
- [ ] Classify findings: Security / Maintainability / Style / False Positive.
- [ ] Prioritize: critical security issues first, then high-impact maintainability issues.
- [ ] Fix one security issue live and rerun scans to show progress.

Presenter notes
- Keep each tool's output visible and explain why each finding matters.
- Emphasize: tools are feedback, not blockers — use them to improve code quality.

## Triage quick guide
- Security (High) — fix immediately.
- Data exposure / secret in code — rotate credentials and remove from history.
- Injection/XSS/command execution — high priority.
- Style (Low) — schedule in regular cleanup or before major release.

## Demo expectations
- Running the demo should produce Bandit warnings (e.g., use of subprocess, weak crypto) and Flake8 issues (unused imports, style). Use the findings to show the triage flow.

## References & tools
- Bandit (security): https://bandit.readthedocs.io
- Flake8 (style): https://flake8.pycqa.org
- GitHub Actions (CI): https://docs.github.com/actions
