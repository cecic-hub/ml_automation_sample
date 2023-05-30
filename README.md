# Introduction
This is a sample Python Project for testing [mall.cz](https://www.mall.cz/)
>There is access denied issue when testing with Chrome, please use Firefox to run the test

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all packages in venv environment.

```bash
pip install -r requirements.txt
```

## Command to run the project

```bash
python -X utf8 -m pytest -k test_check_carousel --html=src/report/pytest-html/report.html --self-contained-html
```

## Project Structure

    .
    ├── pytest_cases                    # Test files
    │   ├── conftest.py                 # Before or after test
    │   └── test_mallcz.py              # Test case
    ├── src                             # Source files
    │   ├── base                        # Config reader and selenium function files
    │   ├── config_file                 # Set configuration
    │   ├── pages                       # Store elements by page
    │   └── report                      # Report files
    │       └── pytest-html             # html reports
    │           └── html_screenshots    # Screenshots in html report
    ├── requirements.txt
    └── README.md

## Configuration
| Flag         | Value                                                                                     |
|--------------|-------------------------------------------------------------------------------------------|
| Driver       | `Firefox` or `Chrome`                                                                     |
| url          | Testing site url                                                                          |
| mobileWeb    | `Y`: Test with mobile screen size <br/>`N`: Test with computer screen size                |
| CloseBrowser | `Y`: Close browser after test <br/>`N`: Do not close browser after test                   |
| headless     | `Y`: Do not display browser when running test <br/>`N`: Display browser when running test |
