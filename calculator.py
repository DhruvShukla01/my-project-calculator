# author: Dhruv Shukla
# date: May 15, 2023
# file: calculator.py a Python program that implements a imfix to postfix function and calculate function for calculator program
# input: user responses (strings) (infix equations)
# output: interactive messages and infix to postfix conversion (latter is used by expression tree and is used again for calculation)

from stack import Stack
from tree import ExpTree


# Function to convert infix expression to postfix expression.
def infix_to_postfix(infix):
    op_stack = Stack()
    # for precedence order
    op_dict = {'^': 0, '*': 1, '/': 1, "+": 2, '-': 2}
    num = ''
    postfix = []
    # iterates through infix expression
    for i in infix:
        # checks for decimal numbers and numbers
        if i.isdigit() or i == '.':
            num += i
        elif not i.isdigit() or i == '.':
            if num:
                postfix.append(num)
            num = ''
            # checks for parenthesis and deals with them
            if i == '(':
                op_stack.push(i)
            elif i == ')':
                top_element = op_stack.pop()
                while top_element != '(':
                    postfix.append(top_element)
                    top_element = op_stack.pop()
            else:
                if i != '(':
                    while not op_stack.isEmpty() and op_stack.peek() != '(' and op_stack.peek() in op_dict and op_dict[
                        op_stack.peek()] <= op_dict[i]:
                        postfix.append(op_stack.pop())
                    op_stack.push(i)
    if num:
        postfix.append(num)
    while '' in postfix:
        postfix.remove('')
    while op_stack.isEmpty() == False:
        postfix.append(op_stack.pop())
    return " ".join(postfix)


# calculates the infix expression
def calculate(infix):
    i = infix
    p = infix_to_postfix(i)
    # splits the string into a list
    x = ExpTree.make_tree(p.split())
    exp_eval = ExpTree.evaluate(x)
    return exp_eval


# a driver to test calculate module
if __name__ == '__main__':
    print(f"Welcome to Calculator Program!")
    # executes main interactive part of the program
    while True:
        usr_input = input(f"Please enter your expression here. To quit enter 'quit' or 'q':")
        usr_input = usr_input.lower()
        if usr_input == 'q' or usr_input == 'quit':
            print(f"\nGoodbye!")
            break
        print(f"\n{calculate(usr_input)}")

    # test infix_to_postfix function
    assert infix_to_postfix('(5+2)*3') == '5 2 + 3 *'
    assert infix_to_postfix('5+2*3') == '5 2 3 * +'

    # test calculate function
    assert calculate('(5+2)*3') == 21.0
    assert calculate('5+2*3') == 11.0
