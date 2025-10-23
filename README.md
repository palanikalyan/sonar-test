# Static Analysis Workshop Demo

Quick starter for the workshop demo. It contains a tiny Python app with intentional issues to demonstrate Bandit (security) and Flake8 (style) findings locally and in CI.

Try it locally (Windows PowerShell):

1. Clone the repo and open PowerShell in the repo root.
2. Run:

```powershell
.\run_scans.ps1
```

3. Inspect the Bandit and Flake8 output. To run the app with an environment secret:

```powershell
$env:API_SECRET = 'supersecret'
.\venv\Scripts\python.exe demo_app\app.py
```

CI: Push a branch or open a PR to trigger `.github/workflows/static-analysis.yml`.

Expected findings:
- Bandit: warnings about use of shell=True, weak hash (MD5), and printing secrets.
- Flake8: style errors (unused imports, line length, etc.)

SonarCloud quick setup
- Create a project in SonarCloud (https://sonarcloud.io) and note your organization key.
- In your repo settings, add repository secrets `SONAR_ORG` (your org key) and `SONAR_TOKEN` (Sonar login token).
- The workflow `.github/workflows/sonarcloud.yml` will run on push/PR and push results to SonarCloud.
