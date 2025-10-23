# Running SonarScanner on this demo repo

If SonarQube isn't flagging the vulnerable file, it may be because the project isn't configured to include `demo_app` or the scanner run excludes it. This file shows simple ways to run the SonarScanner and troubleshoot.

Prerequisites
- A SonarQube server (local or remote) or SonarCloud account.
- Sonar token for authentication (if remote).

1) Quick check: ensure `sonar-project.properties` exists in repo root and `sonar.sources` includes `demo_app` (this repo includes one).

2) Run with SonarScanner Docker image (no local install):

```powershell
# Replace SONAR_HOST_URL and SONAR_TOKEN with your values
$env:SONAR_HOST_URL = 'http://localhost:9000'
$env:SONAR_TOKEN = 'YOUR_TOKEN'

docker run --rm -e SONAR_HOST_URL=$env:SONAR_HOST_URL -e SONAR_LOGIN=$env:SONAR_TOKEN \
  -v ${PWD}:/usr/src -w /usr/src sonarsource/sonar-scanner-cli
```

3) Run SonarScanner locally (if installed):

```powershell
sonar-scanner -Dsonar.login=YOUR_TOKEN -Dsonar.host.url=http://localhost:9000
```

4) GitHub Actions: add the official SonarCloud/Scanner action and ensure `sonar.sources` includes `demo_app`. Example step (in your workflow):

```yaml
- name: SonarScanner
  uses: sonarsource/sonarcloud-github-action@v1
  with:
    args: >
      -Dsonar.login=${{ secrets.SONAR_TOKEN }}
```

Troubleshooting
- If no issues appear: check the Sonar project dashboard and verify the files analyzed list contains `demo_app/sonar_bad.py`.
- Confirm file inclusion: Sonar excludes files matching patterns in `sonar.exclusions` or global server settings. Check server-level exclusions.
- If using SonarCloud, ensure the project key matches and you authorized organization/repo access.
- Rerun the scanner with `-X` to get debug logs and confirm which files were scanned.

If you'd like, I can add a ready-to-run GitHub Actions workflow that runs Sonar scanner and uploads results (you'll still need to provide `SONAR_TOKEN` in repo secrets).
