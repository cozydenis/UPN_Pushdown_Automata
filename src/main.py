import time

# numbers to test
# 3 1 + 7 8 + 9 8 7 + 1 2 1 4 + + 7 + + + + + +
# 3 4 + 6 2 + 8 9 + 4 3 + * * *
# 3 4 + *
# 8 + 9 + 7 * 2 *
#
#

class Stack:
    """
    A simple implementation of a stack data structure providing essential stack operations.
    """
    def __init__(self):
        self.stack = []

    def push(self, item):
        """
        Pushes an item onto the top of the stack.

        :param item: The item to be pushed onto the stack.
        """
        self.stack.append(item)

    def pop(self):
        """
        Removes and returns the item at the top of the stack.

        :return: The item at the top of the stack.
        """
        return self.stack.pop()

    def is_empty(self):
        """
        Checks if the stack is empty.

        :return: True if the stack is empty, False otherwise.
        """
        return len(self.stack) == 0


class PushdownAutomata:
    """
    Utilizes a stack to evaluate mathematical expressions written in Reverse Polish Notation.
    """
    def __init__(self):
        """
        Initializes the Pushdown Automata with an empty stack.
        """
        self.stack = Stack()
        self.mode = 0

    def calculate(self, expression, mode):
        """
        Evaluates a mathematical expression provided in Reverse Polish Notation.

        :param expression: A string representing the mathematical expression in RPN.
        :param mode: An integer indicating the operation mode (0 for Fast-Mode, 1 for Step-Mode).
        :return: The result of the evaluated expression or an error message if the notation is invalid.
        """

        self.stack.stack = []
        tokens = expression.split()
        self.mode = mode

        for token in tokens:
            if token.isdigit():
                self.stack.push(int(token))
                if self.mode == 1:
                    print(f"Pushed to stack: {token}")
                    print(f"Current stack: {self.stack.stack}")
                    time.sleep(1)

            elif self.isOperator(token):
                if len(self.stack.stack) < 2:
                    return "Invalid notation: not enough operands for operator"

                operand2 = self.stack.pop()
                operand1 = self.stack.pop()

                if self.mode == 1:
                    print(f"Pop for operation: {operand1}, {operand2}")
                    time.sleep(1)

                result = self.performOperation(operand1, operand2, token)

                self.stack.push(result)

                if self.mode == 1:
                    print(f"Operation: {operand1} {token} {operand2} = {result}")
                    print(f"Stack after operation: {self.stack.stack}")
                    time.sleep(1)

        if len(self.stack.stack) != 1:
            return "Invalid notation: stack should contain exactly one element at the end, but has: {}".format(self.stack.stack)

        return self.stack.pop()

    def performOperation(self, operand1, operand2, operator):
        """
        Performs the specified arithmetic operation on two operands.

        :param operand1: The first operand.
        :param operand2: The second operand.
        :param operator: A character representing the arithmetic operation (+, -, *, /).
        :return: The result of the arithmetic operation.
        """

        if operator == '+':
             return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return operand1 / operand2

    def isOperator(self, token):
        """
        Checks if a given token is an arithmetic operator.

        :param token: The token to check.
        :return: True if the token is an operator, False otherwise.
        """
        return token in ('+', '-', '*', '/')

def main():
    pda = PushdownAutomata()
    mode = 0 # 0 for Fast-Mode 1 for Step-Mode
    print("******************************************************************")
    print("*                                                                *")
    print("*     Welcome to the Reverse Polnish Notation Calculator!        *")
    print("*                                                                *")
    print("******************************************************************")

    while True:
        while True:
            userInputMode = input("Choose Mode  1. Fast-Mode 2. Step-Mode (or 'q' to quit): ")
            if userInputMode.lower().isdigit():
                mode = int(userInputMode.lower()) - 1


                break
            elif userInputMode.lower() == 'q':
                exit()

            else:
                print("Invalid mode. Please enter a number.")

        expression = input("UPN Notation (or 'q' to quit): ")
        if expression.lower() == 'q':
            break
        print(pda.calculate(expression, mode))

if __name__ == "__main__":
    main()