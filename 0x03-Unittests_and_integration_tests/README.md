
# 0x03. Unittests and Integration Tests

## Table of Contents

- [Description](#description)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Resources](#resources)
- [Project Structure](#project-structure)
- [Tasks](#tasks)
  - [Mandatory Tasks](#mandatory-tasks)
  - [Advanced Tasks](#advanced-tasks)
- [Usage](#usage)
- [Author](#author)

---

## Description

This project focuses on writing **unit tests** and **integration tests** in Python. The goal is to:

- Test individual units of code for correctness.
- Test the interactions between different parts of the codebase to ensure they work as expected.

Unit testing is primarily focused on testing small parts (units) of code in isolation, whereas integration tests validate the end-to-end functionality of the system.

## Learning Objectives

By the end of this project, you should be able to:

- Explain the difference between unit tests and integration tests.
- Utilize common testing patterns such as mocking, parameterization, and fixtures.
- Create efficient and effective test cases for Python functions and classes.

---

## Requirements

- **Python version**: Python 3.7
- **Operating System**: Ubuntu 18.04 LTS
- **Style Guide**: Pycodestyle (v2.5)
- All files should be executable and end with a new line.
- All modules, classes, and functions must include proper documentation.
- All functions and coroutines must have type annotations.

---

## Resources

- [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
- [unittest.mock — Mock object library](https://docs.python.org/3/library/unittest.mock.html)
- [Parameterized](https://pypi.org/project/parameterized/)
- [Memoization](https://en.wikipedia.org/wiki/Memoization)

---

## Project Structure

```plaintext
0x03-Unittests_and_integration_tests/
├── README.md
├── utils.py
├── client.py
├── fixtures.py
├── test_utils.py
└── test_client.py
```

- **utils.py**: Contains utility functions such as `access_nested_map` and `get_json`.
- **client.py**: Contains the `GithubOrgClient` class for interacting with GitHub organizations.
- **fixtures.py**: Provides pre-defined data fixtures for integration testing.
- **test_utils.py**: Unit tests for `utils.py`.
- **test_client.py**: Unit and integration tests for `client.py`.

---

## Tasks

### Mandatory Tasks

1. **Parameterize a unit test**
    - Write parameterized tests for `utils.access_nested_map` to validate it returns the expected values or raises `KeyError`.

2. **Parameterize exceptions**
    - Test that `utils.access_nested_map` raises the correct exceptions for invalid inputs.

3. **Mock HTTP calls**
    - Mock external HTTP calls in `utils.get_json` and validate behavior.

4. **Memoize tests**
    - Test the behavior of the `utils.memoize` decorator to ensure it caches function results.

5. **Mocking a property**
    - Mock the `GithubOrgClient._public_repos_url` property and test its behavior.

6. **Test public repos**
    - Mock and test the `GithubOrgClient.public_repos` method, ensuring it retrieves the expected repositories.

7. **Test licensing**
    - Validate that `GithubOrgClient.has_license` correctly identifies repositories with specific licenses.

8. **Integration test: Fixtures**
    - Use fixtures from `fixtures.py` to test interactions between methods in `GithubOrgClient`.

### Advanced Tasks

1. **Integration tests**
    - Write integration tests for `GithubOrgClient.public_repos` and `public_repos_with_license` using the provided fixtures.

---

## Usage

### Running Tests

To execute the test cases, run the following command:

```bash
python3 -m unittest path/to/test_file.py
```

For example:

```bash
python3 -m unittest test_utils.py
```

### Code Style

Ensure the code adheres to the `pycodestyle` standard:

```bash
pycodestyle path/to/file.py
```

---

## Author

- **Name:** Refiloe Radebe
- **GitHub Repository: [alx-backend-python](https://github.com/kweenDev/alx-backend-python/tree/main/0x03-Unittests_and_integration_tests)
