# Python - Variable Annotations

This repository contains solutions to tasks related to Python's advanced type annotations. The tasks focus on using type hints in Python 3 to specify function signatures, variables, and applying duck typing principles. Additionally, the project involves validating the code with `mypy`, ensuring adherence to PEP 8 standards.

## Project Overview

In this project, I implemented several Python scripts that demonstrate the use of type annotations. These include annotating variables and functions with specific types like `float`, `int`, `str`, and more complex types such as `List`, `Tuple`, and `Union`. The project also introduces duck typing, a concept in Python that allows for flexible and reusable code.

## Learning Objectives

At the end of this project, I was able to:

- Understand Python 3 type annotations.
- Use type annotations to specify function signatures and variable types.
- Grasp the concept of duck typing in Python.
- Validate code using `mypy` for type checking.

## Requirements

- Python 3.7 or later
- Ubuntu 18.04 LTS
- Code must follow the `pycodestyle` (version 2.5) guidelines
- All modules, classes, and functions must contain documentation
- All files must be executable

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/kweendev/alx-backend-python.git
   ```

2. Navigate to the project directory:

   ```bash
   cd alx-backend-python/0x00-python_variable_annotations
   ```

3. Make Python files executable:

   ```bash
   chmod +x *.py
   ```

## Usage

Each script in this project can be executed from the terminal. The main Python scripts provided for each task will import and test the corresponding function. For example:

1. **Task 0**: Basic annotations for addition

   - Run the following command to test the `add` function:

   ```bash
   ./0-main.py
   ```

2. **Task 1**: String concatenation

   - To test the `concat` function, run:

   ```bash
   ./1-main.py
   ```

## Files

| Filename                    | Description                                                                      |
| --------------------------- | -------------------------------------------------------------------------------- |
| `0-add.py`                  | A function that adds two floats and returns the result as a float.               |
| `1-concat.py`               | A function that concatenates two strings.                                        |
| `2-floor.py`                | A function that returns the floor of a float.                                    |
| `3-to_str.py`               | A function that returns the string representation of a float.                    |
| `4-define_variables.py`     | Annotates several variables with specific types and values.                      |
| `5-sum_list.py`             | A function that returns the sum of a list of floats.                             |
| `6-sum_mixed_list.py`       | A function that sums a list containing both floats and integers.                 |
| `7-to_kv.py`                | A function that returns a tuple with a string and the square of an int or float. |
| `8-make_multiplier.py`      | A function that returns a function to multiply a float by a multiplier.          |
| `9-element_length.py`       | Annotates a function that returns a list of tuples (sequence, length).           |
| `100-safe_first_element.py` | A duck-typed function that returns the first element or `None`.                  |
| `101-safely_get_value.py`   | Annotates a function that safely retrieves a dictionary value.                   |
| `102-type_checking.py`      | Annotates a function that zooms in an array (using mypy for validation).         |

## Example

Here’s an example of the output from running the `0-main.py` script:

```bash
$ ./0-main.py
True
{'a': <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}
```

## Author

_Refiloe Radebe_
