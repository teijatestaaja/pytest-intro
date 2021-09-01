# Learning pytest

See [https://docs.pytest.org](https://docs.pytest.org)

## I learned the following

 - basic test case, pass / fail
 - assertions
 - exceptions
 - parameterized tests (@pytest.mark.parametrize)
 - testing classes
 - fixtures (@pytest.fixtures)
 - commands and configs
 - filtering and marking tests (@pytest.mark.insert_mark_here)
 - feature tests (alternately: "black box" tests, "integration tests", "end-to-end" tests, "system" tests)
 - testing REST APIs with requests package
 - extending pytest with plugins (for reporting: pytest-html, for code coverage: pytest-cov, for parallel test run: xdist)

## Commands

```code
explore commands:
    python -m pytest --help

run all tests:
    python -m pytest

run tests only in a module:
    python -m pytest tests/test_modulename.py

run a single test case in a module:
    python -m pytest tests/test_modulename.py::test_casename

run all test cases that contain word "my_test"
    python -m pytest -k my_test

run all test cases that are marked with custom marker "smoke", defined at config file
    python -m pytest -m smoke

run tests with pytest-html for reporting:
    python -m pytest --html=path_to/report.html

run tests with pytest-cov for code coverage on product code (not tests):
    python -m pytest --cov=path_to/folder_name

generate html report for code coverage:
    python -m pytest -cov=path_to/folder_name --cov-report html
```