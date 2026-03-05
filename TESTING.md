\# Testing Strategy



This project uses both \*\*unit testing\*\* and \*\*integration testing\*\* to verify the functionality of the Quick-Calc application.



---



\## What Was Tested



The following components were tested:



\* Individual arithmetic operations (addition, subtraction, multiplication, division)

\* Edge cases such as division by zero

\* Negative numbers and decimal values

\* Interaction between the CLI interface and calculator logic



---



\## What Was Not Tested



Non-functional aspects such as performance, usability, and scalability were not tested.

This project focuses primarily on verifying the \*\*functional correctness\*\* of the calculator operations.



---



\## Testing Pyramid



The testing pyramid recommends having many unit tests and fewer integration tests.



This project follows this structure:



\* \*\*8 Unit Tests\*\*

\* \*\*2 Integration Tests\*\*



Unit tests verify individual methods of the calculator class, while integration tests ensure that the CLI interface correctly interacts with the calculator logic.



---



\## Black-Box vs White-Box Testing



Unit tests primarily use \*\*white-box testing\*\*, because they directly test internal functions and logic of the calculator.



Integration tests use a \*\*black-box testing\*\* approach because they test the system from the perspective of user interaction without focusing on internal implementation.



---



\## Functional vs Non-Functional Testing



The tests implemented in this project focus on \*\*functional testing\*\*, verifying that the calculator performs mathematical operations correctly.



Non-functional testing such as performance or load testing was not included because it is outside the scope of this assignment.



---



\## Regression Testing



The test suite can also act as a \*\*regression testing tool\*\*.

If new features are added in the future, running the existing tests ensures that previously working functionality has not been broken.



---



\## Test Results Summary



| Test Name                    | Type        | Status |

| ---------------------------- | ----------- | ------ |

| test\_addition                | Unit        | Pass   |

| test\_subtraction             | Unit        | Pass   |

| test\_multiplication          | Unit        | Pass   |

| test\_division                | Unit        | Pass   |

| test\_negative\_numbers        | Unit        | Pass   |

| test\_decimal\_numbers         | Unit        | Pass   |

| test\_large\_numbers           | Unit        | Pass   |

| test\_divide\_by\_zero          | Unit        | Pass   |

| test\_user\_addition\_flow      | Integration | Pass   |

| test\_clear\_after\_calculation | Integration | Pass   |



