# \# Quick-Calc

# 

# Quick-Calc is a simple calculator application developed for a Software Engineering testing assignment.

# It performs basic arithmetic operations and demonstrates good software testing practices using Python.

# 

# \## Features

# 

# \* Addition

# \* Subtraction

# \* Multiplication

# \* Division (with division-by-zero handling)

# \* Clear function

# 

# ---

# 

# \## Setup Instructions

# 

# 1\. Install \*\*Python 3.10 or newer\*\*

# 2\. Clone the repository

# 

# ```

# git clone https://github.com/sin8810/swe-testing-assignment.git

# ```

# 

# 3\. Navigate to the project directory

# 

# ```

# cd swe-testing-assignment

# ```

# 

# 4\. Install dependencies

# 

# ```

# py -m pip install pytest

# ```

# 

# ---

# 

# \## Running the Application

# 

# The core calculator logic is implemented in:

# 

# ```

# calculator.py

# ```

# 

# The interaction layer that connects user inputs to the calculator logic is implemented in:

# 

# ```

# cli.py

# ```

# 

# ---

# 

# \## Running Tests

# 

# Run the full test suite with one command:

# 

# ```

# py -m pytest

# ```

# 

# Expected result:

# 

# ```

# 10 passed

# ```

# 

# ---

# 

# \## Testing Framework Research

# 

# Two Python testing frameworks were considered for this project: \*\*Pytest\*\* and \*\*Unittest\*\*.

# 

# \### Pytest

# 

# Pytest is a modern testing framework designed to make writing tests simple and readable. Tests are written as simple Python functions using standard `assert` statements. Pytest provides powerful features such as fixtures, parameterized testing, and detailed failure output. It is widely used in professional Python development due to its simplicity and flexibility.

# 

# \### Unittest

# 

# Unittest is Python’s built-in testing framework based on the JUnit architecture. Tests are written inside classes and require more boilerplate code compared to Pytest. While it provides strong structure and is included with Python by default, it can be more verbose and less intuitive for smaller projects.

# 

# \### Final Choice

# 

# Pytest was selected for this project because it provides \*\*simpler syntax, better readability, and faster test development\*\*, which is ideal for small projects like Quick-Calc.

# 

