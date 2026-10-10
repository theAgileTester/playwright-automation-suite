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

## Lessons learned
A few real debugging findings from building this suite:

- **Async/sync conflict in CI**: two legacy scripts using Playwright's
  sync API directly (`sync_playwright()`) clashed with `pytest-playwright`'s
  own event loop once run through `pytest` in CI, despite working fine
  when run standalone. Fixed by excluding them from pytest collection.
- **Race condition in a dynamically-loaded dropdown**: `wait_for_selector(state="attached")`
  only waits for the *first* option to exist, not for the full list to
  finish loading via AJAX — causing intermittent failures reading stale
  option lists. Fixed with `wait_for_function()`, asserting the option
  count explicitly.
- **Order-dependent flakiness on a shared public demo**: a login test
  with an invalid password occasionally succeeded in CI when run
  immediately after a valid-login test, due to the demo app's
  inconsistent session handling — confirmed by isolating the test and
  re-running it alone.

## Regulatory awareness
Testing a banking application also means being aware of the regulatory
context real financial software operates in:

- **GDPR** — governs personal data handling; test data should never be
  real customer data (this project uses ParaBank's public demo
  credentials for exactly this reason).
- **DORA** — requires financial institutions' IT systems to be
  operationally resilient; automated regression suites and CI are part
  of demonstrating that kind of continuous verification.
- **PCI DSS** — security standard for systems handling card data; card
  numbers must never appear in logs, screenshots, or test fixtures.
- **PSD2** — mandates Strong Customer Authentication for payments; a
  production-grade login/transfer test suite would need to cover MFA
  flows, not just username/password.
- **MiFID II** — requires transparency and accurate record-keeping for
  investment services; testing audit trails (e.g. transaction history)
  is a relevant QA concern.

## Status
Core login and transfer flows automated and passing in CI. Actively
expanding coverage.
