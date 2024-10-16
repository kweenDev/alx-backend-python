# 0x02. Python - Async Comprehension

## Project Overview

This project is designed to help you learn and apply asynchronous programming techniques in Python using asynchronous comprehensions and generators. You will work with async functions and the `asyncio` module, implementing asynchronous coroutines and comprehensions to process data efficiently. The goal is to understand how to write and optimize Python programs that perform asynchronous tasks concurrently.

## Learning Objectives

By the end of this project, you will be able to:

- Write asynchronous generators.
- Use asynchronous comprehensions for more efficient code.
- Type-annotate Python generators and comprehensions correctly.

## Resources

To complete this project, the following resources will be useful:

- [PEP 530 – Asynchronous Comprehensions](https://www.python.org/dev/peps/pep-0530/)
- [What’s New in Python: Asynchronous Comprehensions / Generators](https://docs.python.org/3/whatsnew/3.6.html#pep-530-asynchronous-comprehensions)
- [Type-hints for Generators](https://docs.python.org/3/library/typing.html#typing.Generator)

## Project Structure

The project consists of three key tasks, each building on the previous ones to demonstrate various asynchronous techniques in Python.

### Task 0: Async Generator

**File:** `0-async_generator.py`

You will implement a coroutine called `async_generator` that yields 10 random numbers between 0 and 10 asynchronously. The coroutine waits for 1 second before yielding each number.

**Usage:** The function can be called to asynchronously generate 10 numbers over a time span of 10 seconds.

```python
#!/usr/bin/env python3
import asyncio
import random

async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
```

### Task 1: Async Comprehension

**File:** `1-async_comprehension.py`

You will import the `async_generator` function from Task 0 and write a coroutine called `async_comprehension`. This function will collect 10 random numbers using an async comprehension over `async_generator`, then return the list of numbers.

**Usage:** This allows collecting the generated values from `async_generator` in a list asynchronously.

```python
#!/usr/bin/env python3
import asyncio
from typing import List
from 0_async_generator import async_generator

async def async_comprehension() -> List[float]:
    return [i async for i in async_generator()]
```

### Task 2: Run Time for Four Parallel Comprehensions

**File:** `2-measure_runtime.py`

This task involves writing a coroutine called `measure_runtime` that runs `async_comprehension` four times in parallel using `asyncio.gather`. You will measure and return the total time taken to execute all four coroutines.

**Usage:** This demonstrates how to run multiple asynchronous tasks concurrently and measure their overall execution time.

```python
#!/usr/bin/env python3
import asyncio
import time
from 1_async_comprehension import async_comprehension

async def measure_runtime() -> float:
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())
    end_time = time.perf_counter()
    return end_time - start_time
```

## Requirements

- **Python version:** Python 3.7
- **Operating system:** Ubuntu 18.04 LTS
- **Code style:** Follow PEP8 and `pycodestyle` version 2.5.x

Each file should:

- Begin with `#!/usr/bin/env python3`.
- End with a new line.
- Contain proper function and module documentation.
- Include type annotations for all functions and coroutines.

## Setup Instructions

1. Clone the project repository:

```bash
git clone https://github.com/kweenDev/alx-backend-python.git
cd alx-backend-python/0x02-python_async_comprehension
```

2. Ensure you have Python 3.7 installed:

```bash
python3 --version
```

3. Install dependencies if necessary:

```bash
sudo apt update
sudo apt install python3.7
```

4. Run each script with the following commands:

_For Task 0:_

```bash
./0-main.py
```

_For Task 1:_

```bash
./1-main.py
```

_For Task 2:_

```bash
./2-main.py
```

## Testing

You can run tests using Python's `asyncio.run()` to verify the functionality of each task.

- _For Task 0:_
  ```bash
  python3 0-main.py
  ```
- _For Task 1:_
  ```bash
  python3 1-main.py
  ```
- _For Task 2:_
  ```bash
  python3 2-main.py
  ```

## Conclusion

This project serves as an introduction to Python's asynchronous capabilities using generators and comprehensions. By completing the tasks, you'll gain a deeper understanding of how to build and manage asynchronous workflows, run tasks concurrently, and write efficient Python code using `asyncio`.
