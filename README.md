# Quick-Calc

Quick-Calc is a simple calculator application developed for a Software Engineering testing assignment.

It performs basic arithmetic operations using Python.

## Features

- Addition
- Subtraction
- Multiplication
- Division (with division-by-zero handling)
- Clear function

## Setup Instructions

1. Install Python 3.10 or newer
2. Clone the repository

git clone https://github.com/sin8810/swe-testing-assignment.git

3. Navigate to the project directory

cd swe-testing-assignment

4. Install dependencies

py -m pip install pytest

## Running Tests

Run all tests with:

py -m pytest

Expected result:

10 passed

## Testing Framework Research

Two frameworks were considered: Pytest and Unittest.

Pytest is a modern testing framework that allows simple test functions and clear assertions. It provides powerful features like fixtures and detailed failure output.

Unittest is Python’s built-in testing framework based on the JUnit design. It requires more structured test classes and tends to be more verbose.

For this project, Pytest was chosen because it is simpler to use and produces cleaner test code.
