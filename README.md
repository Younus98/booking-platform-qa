# Booking Platform QA

Automated test suite for the [Shady Meadows B&B](https://automationintesting.online) (Restful-Booker Platform), covering both API and UI layers with Python, pytest, Playwright and Requests.

## Project Structure

```
booking-platform-qa/
├── .github/workflows/   # CI pipeline (GitHub Actions)
├── docs/                # Test strategy, defect reports, AI review log
├── pages/               # Page Object Model classes (Playwright)
├── tests/
│   ├── api/             # API tests (requests + JSON validation)
│   └── ui/              # UI tests (Playwright)
├── utils/               # Shared helpers
├── conftest.py          # Global fixtures
├── pytest.ini           # Pytest configuration
└── requirements.txt     # Python dependencies
```

## Prerequisites

- Python 3.13+
- pip

## Setup

```bash
# Clone the repository
git clone https://github.com/Younus98/booking-platform-qa.git
cd booking-platform-qa

# Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS / Linux

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install --with-deps chromium
```

## Running Tests

```bash
# Run all tests
pytest -v

# Run only API tests
pytest tests/api/ -v

# Run only UI tests
pytest tests/ui/ -v

# Generate an HTML report
pytest -v --html=reports/report.html --self-contained-html
```

## CI/CD

Tests run automatically on every push and pull request via GitHub Actions. The workflow installs dependencies, launches Chromium, executes the full suite, and uploads:

- **test-report** — HTML test report
- **failure-evidence** — screenshots and Playwright traces on failure

## Test Approach

| Layer | Tools | Purpose |
|-------|-------|---------|
| API | requests, Cerberus | Business rules, data validation, error responses |
| UI | Playwright (pytest-playwright) | Critical user journeys (room list, contact form) |

The suite follows the test pyramid: many fast API tests, fewer targeted UI tests. Full details are in [docs/test-strategy.md](docs/test-strategy.md).

## Documentation

- [Test Strategy](docs/test-strategy.md)
- [Defect Report](docs/defects.md)
- [AI Review Log](docs/ai-review-log.md)