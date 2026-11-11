# Axa Mandiri Test

Playwright UI tests written in Python and run with pytest against the OrangeHRM
demo site.

## Project structure

```text
config.py
pages/
  add_employee_page.py
  base_page.py
  dashboard_page.py
  login_page.py
  pim_page.py
tests/
  conftest.py
  ui/
    test_orangehrm.py
.env                  # Local credentials; ignored by Git
.env.example          # Credential template
pytest.ini
requirements.txt
```

Test scenarios and assertions belong in `tests/`; page locators and user
actions belong in `pages/`. The employee search and deletion tests create
unique employee records and remove them afterward.

## Setup

Create and activate a virtual environment, then install the project dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m playwright install
```

The local `.env` file contains the demo login credentials and is excluded from
Git. Update it if the demo credentials change. The required variables are:

```env
ORANGEHRM_BASE_URL=https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
ORANGEHRM_USERNAME=your_username
ORANGEHRM_PASSWORD=your_password
```

On Windows, activate the environment with `.venv\Scripts\activate`.

## Run tests

```bash
pytest tests/ui
```

Playwright runs browsers headlessly by default. To see the browser while testing:

```bash
pytest tests/ui --headed
```

To run one scenario, specify its test name:

```bash
pytest tests/ui/test_orangehrm.py::test_login_with_valid_credentials_opens_dashboard
```
