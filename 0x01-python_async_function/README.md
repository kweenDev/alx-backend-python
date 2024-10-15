# 0x01. Python - Async

## Overview

This project explores asynchronous programming in Python using `asyncio`. You will learn how to create asynchronous coroutines, run them concurrently, and manage tasks. The focus is on understanding how `async` and `await` work, how to execute coroutines in parallel, and how to manage tasks efficiently in Python.

## Learning Objectives

By the end of this project, you should be able to:

- Understand `async` and `await` syntax in Python.
- Execute asynchronous programs with `asyncio`.
- Run multiple coroutines concurrently.
- Create and manage asyncio tasks.
- Use the `random` module in asynchronous functions.

## Project Structure

```bash
0x01-python_async_function/
├── 0-basic_async_syntax.py
├── 1-concurrent_coroutines.py
├── 2-measure_runtime.py
├── 3-tasks.py
├── 4-tasks.py
└── README.md
```

## Requirements

- Python 3.7 or later.
- All your code should be executed on Ubuntu 18.04 LTS using `python3`.
- You must adhere to `pycodestyle` (version 2.5.x) style for Python code.
- Each Python module should contain module-level documentation, and each function must be properly documented as well.
- All coroutines and functions must be type-annotated.
- Your Python scripts must be executable.

## Files Description

### 0. **The Basics of Async**

##### File: `0-basic_async_syntax.py`

This script contains an asynchronous coroutine, `wait_random`, that takes an integer argument `max_delay` (default value of 10) and waits for a random delay between `0` and `max_delay` (inclusive). After the wait, it returns the delay.

#### Example Usage:

```python
#!/usr/bin/env python3

import asyncio
from 0_basic_async_syntax import wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
```

### 1. **Let's Execute Multiple Coroutines**

##### File: `1-concurrent_coroutines.py`

This script contains an async function, `wait_n`, that takes two integer arguments `n` and `max_delay`. It spawns `wait_random` `n` times, with the specified `max_delay`, and returns a list of the delays in ascending order without using the `sort()` method.

#### Example Usage:

```python
#!/usr/bin/env python3

import asyncio
from 1_concurrent_coroutines import wait_n

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
```

### 2. **Measure the Runtime**

##### File: `2-measure_runtime.py`

This script contains a `measure_time` function that takes integers `n` and `max_delay`. It measures the total execution time for `wait_n(n, max_delay)` and returns the average time taken per coroutine.

#### Example Usage:

```python
#!/usr/bin/env python3

from 2_measure_runtime import measure_time

n = 5
max_delay = 9

print(measure_time(n, max_delay))
```

### 3. **Tasks**

##### File: `3-tasks.py`

This script contains a function `task_wait_random`, which takes an integer `max_delay` and returns an `asyncio.Task` that wraps the `wait_random` coroutine.

#### Example Usage:

```python
#!/usr/bin/env python3

import asyncio
from 3_tasks import task_wait_random

async def test(max_delay: int):
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))
```

### 4. **Tasks (Modified wait_n)**

##### File: `4-tasks.py`

This file contains the `task_wait_n` function, which modifies the `wait_n` function to use the `task_wait_random` function from the previous task. It behaves similarly to `wait_n` but returns the list of delays using tasks.

#### Example Usage:

```python
#!/usr/bin/env python3

import asyncio
from 4_tasks import task_wait_n

print(asyncio.run(task_wait_n(5, 6)))
```

## Installation and Setup

1. Clone the repository to your local machine:

```bash
git clone https://github.com/kweendev/alx-backend-python.git
```

2. Navigate to the project directory:

```bash
cd 0x01-python_async_function
```

3. Ensure that your Python environment is set up:

```bash
python3 -m venv venv
source venv/bin/activate
```

4. Install any necessary packages:

```bash
pip install -r requirements.txt
```

### Running the Files

Each task can be run by executing the corresponding Python file:

```bash
chmod +x <file>.py
./<file>.py
```

**For example**:

```bash
./0-main.py
```

## Author

_Refiloe Radebe_
