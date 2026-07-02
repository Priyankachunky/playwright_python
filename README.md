# Python Playwright POM Framework

This workspace contains a clean Python Playwright setup that follows the Page Object Model (POM) and supports data-driven testing through JSON/CSV loaders.

## Structure
- `pages/` contains reusable page objects.
- `tests/` is reserved for test modules.
- `data/` stores JSON or CSV test data.
- `utils/` contains helper functions for loading data.

## Setup
```bash
python -m pip install -r requirements.txt
python -m playwright install chromium
```

## Usage
- Add new page objects under `pages/`.
- Add test data files under `data/`.
- Create test modules under `tests/`.

No sample test files are included.
