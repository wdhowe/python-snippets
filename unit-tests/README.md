# Python Snippets - unit-tests

Unit test examples.

----

## Files

- db_data.json -> Pretend database file used in distrodb_class.py
- distrodb_class.py -> Class to test.
- test_distrodb_class_fixture.py -> Testing distrodb with pytest's fixture
- test_distrodb_class_setup_teardown.py -> Testing distrodb with setup/teardown functions
- my_math.py -> Simple math calculations in order to use with test_my_math.py
- test_my_math.py -> Example unit tests, run tests with: 'pytest -v test_my_math.py'
- test_with_decorators_my_math.py -> -> Example unit tests with decorators
- test_with_parametrize.py -> Example unit tests with parameters

----

## Pytest Examples

Some pytest examples to use with the unit tests in this directory.

### Install Pytest

Install pytest
```bash
pip3 install pytest
```

### Testing Code with Pytest

Test all 'test_*' files in the current directory
```bash
pytest -v
```

Test a single file
```bash
pytest -v test_my_math.py
```

Test a single function inside of a single file
```bash
pytest -v test_my_math.py::test_add_it
```

Test all functions in a file that match a keyword
```bash
pytest -v test_my_math.py -k "add_it"
```

Test all functions that have the custom mark decorator "@pytest.mark.groupA"
```bash
pytest -v test_with_decorators_my_math.py -m "groupA"
```

Register custom markers to avoid warnings
```bash
vim ~/pytest.ini

[pytest]
markers =
  groupA: Mark a test as part of groupA
  groupB: Mark a test as part of groupB
```

