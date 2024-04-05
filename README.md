# Pushdown Automata for Evaluating Reverse Polish Notation Expressions

This project implements a Pushdown Automata (PDA) in Python to evaluate mathematical expressions written in Reverse Polish Notation (RPN). RPN is a notation in which every operator follows all of its operands. It is also known as postfix notation.

## Features

- Evaluate expressions written in Reverse Polish Notation (RPN).
- Supports basic arithmetic operations: addition (+), subtraction (-), multiplication (*), and division (/).
- Two modes of operation:
  - Fast-Mode: Quickly evaluates the expression without detailed output.
  - Step-Mode: Evaluates the expression step-by-step, showing the contents of the stack after each operation.

## How to Use

1. Run the `main()` function in the script.
2. When prompted, choose the operation mode:
   - Enter `1` for Fast-Mode.
   - Enter `2` for Step-Mode.
3. Input your expression in Reverse Polish Notation.
   - Example: `3 4 + 2 *` represents the expression (3 + 4) * 2.
4. To exit, type `q` when prompted for an expression.

## Implementation Details

- The `Stack` class provides basic stack functionalities: `push`, `pop`, and `is_empty`.
- The `PushdownAutomata` class uses the `Stack` class to evaluate the RPN expressions. It supports two modes of operation to either directly evaluate the expression or step through the evaluation process.
