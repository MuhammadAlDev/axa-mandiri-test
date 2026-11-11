# Axa Mandiri Test

Playwright browser tests written in Python and run with pytest.

## Project structure

```text
pages/
  base_page.py       # Shared browser/page operations
  example_page.py   # Locators and actions for an example page
tests/
  test_example.py   # Test scenarios and assertions
pytest.ini
requirements.txt
```

Put **test cases and assertions** in `tests/`. Put each screen's **locators
and user actions** in a page object under `pages/`. Tests should use page
objects instead of defining selectors directly. The example uses in-memory
HTML, so it can run without a target website; replace it with page objects
for the actual application when its URL and selectors are known.

## Setup

Create and activate a virtual environment, then install the project dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m playwright install
```

On Windows, activate the environment with `.venv\Scripts\activate`.

## Run tests

```bash
pytest
```

Playwright runs browsers headlessly by default. To see the browser while testing:

```bash
pytest --headed
```

Add test modules under `tests/` using the `test_*.py` naming convention. The
`page` fixture is provided by `pytest-playwright`. Create additional page
objects under `pages/` and pass the fixture to them, for example
`LoginPage(page)`.
