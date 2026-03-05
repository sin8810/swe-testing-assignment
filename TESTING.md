# Testing Strategy

This document describes the testing approach used for the Quick-Calc calculator application.

## What Was Tested

The following components were tested:

* Addition operation
* Subtraction operation
* Multiplication operation
* Division operation
* Division by zero handling
* Negative numbers
* Decimal numbers
* Large numbers
* Interaction between the CLI interface and calculator logic
* Clear function behavior

## What Was Not Tested

The project focuses on **functional correctness**, so the following were not tested:

* Performance testing
* Security testing
* User interface design
* Load or stress testing

These areas are outside the scope of this assignment.

## Testing Pyramid

The project follows the concept of the **Testing Pyramid**, which suggests having many unit tests and fewer integration tests.

Test distribution in this project:

* **8 Unit Tests**
* **2 Integration Tests**

Unit tests verify individual functions of the calculator, while integration tests verify that different parts of the application work correctly together.

## Black-Box vs White-Box Testing

Two testing approaches were applied in this project.

**White-Box Testing (Unit Tests)**
Unit tests directly access internal calculator functions and verify their outputs. This means the internal implementation of the code is known during testing.

**Black-Box Testing (Integration Tests)**
Integration tests simulate how a user interacts with the calculator without focusing on internal code implementation.

## Functional vs Non-Functional Testing

The project mainly focuses on **functional testing**, verifying that mathematical operations produce correct results.

Non-functional aspects such as performance, usability, and scalability were not tested because they are outside the scope of this assignment.

## Regression Testing

The test suite can also act as a **regression testing tool**.
If the calculator is updated or new features are added in the future, running the existing test suite ensures that previously working functionality has not been broken.

## Test Results Summary

| Test Name                    | Type        | Status |
| ---------------------------- | ----------- | ------ |
| test_addition                | Unit        | Pass   |
| test_subtraction             | Unit        | Pass   |
| test_multiplication          | Unit        | Pass   |
| test_division                | Unit        | Pass   |
| test_negative_numbers        | Unit        | Pass   |
| test_decimal_numbers         | Unit        | Pass   |
| test_large_numbers           | Unit        | Pass   |
| test_divide_by_zero          | Unit        | Pass   |
| test_user_addition_flow      | Integration | Pass   |
| test_clear_after_calculation | Integration | Pass   |
