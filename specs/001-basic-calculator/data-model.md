# Data Model: Basic Calculator

## Entities

The calculator primarily deals with primitive data types, not complex entities. The data model can be described as follows:

- **Expression**: A string representing the mathematical expression to be evaluated.
- **Number**: A floating-point number (`float`) used in calculations.
- **Operation**: A character representing a mathematical operation (+, -, *, /, **).

## State Transitions

The application is stateless in terms of data storage. Each input expression is processed independently. The application state is limited to the current input and the result of the last calculation.
