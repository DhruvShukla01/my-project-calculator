# Calculator Program with GUI

This suite, authored by **Dhruv Shukla** on May 15, 2023, provides both a command-line and a GUI-based calculator for performing mathematical operations. The core functionality allows users to convert and evaluate infix expressions, while the GUI offers an interactive and user-friendly experience.

<img width="465" alt="Screenshot 2023-08-14 at 4 49 12 AM" src="https://github.com/DhruvShukla01/myproject-calculator-python/assets/135282874/8a35f69b-22a4-4469-a8fa-e9e4391a19cb">
<img width="520" alt="Screenshot 2023-08-14 at 4 50 53 AM" src="https://github.com/DhruvShukla01/myproject-calculator-python/assets/135282874/6fec283f-d0bf-477e-8748-25839f86191e">

## Files & Descriptions

### 1. `stack.py`
- **Purpose**: Implements the stack data structure essential for other modules.
- **Input**: User equation from `calculator.py`.
- **Output**: Generates stacks for use in `calculator.py` and `tree.py`.

### 2. `tree.py`
- **Purpose**: Handles binary and expression trees necessary for evaluating the infix equations.
- **Input**: Postfix equation from `calculator.py`.
- **Output**: Constructs an expression tree, evaluates it, and returns its inorder equation.

### 3. `calculator.py`
- **Purpose**: The heart of the calculator suite, providing methods to convert infix expressions to postfix and to calculate the resulting expression.
- **Input**: User's infix equation strings.
- **Output**: Conversion results and final calculation.

### 4. `calculatorGUI.py`
- **Purpose**: Provides a graphical user interface for the calculator, with clickable buttons and a visual display.
- **Input**: User-inputted equations via the GUI.
- **Output**: Displayed calculations within the GUI.

## Features

1. **Infix to Postfix Conversion**: Seamlessly converts user-inputted infix expressions to postfix notation.
2. **Expression Trees**: Constructs and evaluates expression trees to accurately calculate mathematical equations.
3. **Interactive CLI**: Users can interactively input their mathematical expressions and receive calculated results or feedback.
4. **Graphical User Interface**: Offers an intuitive, button-based interface for inputting equations and viewing results. Buttons include standard numbers (0-9), mathematical operations (+, -, *, /), a clear function (c), and equals (=) to calculate results.
5. **Extendability**: With modular Python classes, this suite can be expanded or integrated into larger projects.

## Usage

1. To use the **command-line calculator**:
```bash
python calculator.py
```
2. To use the **GUI calculator**:
 ```bash
python GUIcalculator.py
```
## Testing
Each module (stack.py, tree.py, calculator.py, and calculatorGUI.py) contains a driver program at the bottom which can be used to validate the code and understand its operation.

## Improvements and Bug Fixes
Contributions are welcome! Please fork the repository and open a pull request to add more features, levels, or any other enhancement.

## Licences
This project is licensed under the [MIT License](LICENSE).
