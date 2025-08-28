# README.md

# Python Playwright Tests

This project is a Python-based testing framework that utilizes Playwright for browser automation and pytest for running tests. It follows the Page Object Model design pattern to organize test code and improve maintainability.

## Project Structure

```
python-playwright-tests
├── src
│   ├── pages
│   │   ├── __init__.py
│   │   ├── base_page.py
│   │   └── home_page.py
├── tests
│   ├── __init__.py
│   ├── conftest.py
│   └── test_home.py
├── scripts
│   └── install.py
├── requirements.txt
├── pytest.ini
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd python-playwright-tests
   ```

2. Install the required dependencies:
   ```bash
   python scripts/install.py
   ```

3. Run the tests:
   ```bash
   pytest
   ```

## Usage

- The `src/pages` directory contains the page objects that represent the different pages of the application.
- The `tests` directory contains the test cases that utilize the page objects to perform actions and assertions.
- Use the `scripts/install.py` script to install necessary dependencies.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.