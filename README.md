# Playwright Test Automation Suite

[![Run Playwright Tests](https://github.com/theAgileTester/playwright-automation-suite/actions/workflows/tests.yml/badge.svg)](https://github.com/theAgileTester/playwright-automation-suite/actions/workflows/tests.yml)

A Python + Playwright UI test automation project using Behaviour-Driven
Development (BDD), built as part of an AI Tester career-transition
learning track.

## Purpose
End-to-end UI test automation against a public demo banking application
(ParaBank), covering login and funds-transfer flows — both positive and
negative scenarios — with a CI pipeline that runs the full suite on
every push.

## What's covered
- **Login**: valid credentials, invalid password
- **Transfer Funds**: successful transfer between accounts, validation
  error on empty amount
- Scenarios written in Gherkin (`features/*.feature`), implemented with
  `pytest-bdd` step definitions

## Tools
- Python
- Playwright (sync API)
- pytest + pytest-bdd (BDD / Gherkin)
- GitHub Actions (CI)

## Running locally
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install --with-deps chromium
pytest -v
```

## CI
Every push to `main` runs the full suite headless via GitHub Actions
(see `.github/workflows/tests.yml`). A small number of legacy
exploratory scripts (pre-BDD) are excluded from CI collection via
`pytest.ini`, since they predate the fixture-based test structure.

## Known limitations
ParaBank's public demo is a shared, stateful environment — account
numbers and some backend validations aren't fully deterministic across
runs. Tests are written to read account data dynamically from the page
rather than hardcoding values, to stay resilient to this.

## Status
Core login and transfer flows automated and passing in CI. Actively
expanding coverage.
