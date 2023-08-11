# author: Dhruv Shukla
# date: May 15, 2023
# file: tree.py makes binary and expression tree for calculation of the infix equations
# input:postfix equation from calculator.py
# output: makes expression tree, evaluates it and returns its inorder equation

from stack import Stack


# makes a binary tree
class BinaryTree:
    def __init__(self, rootObj=None):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    # function to insert left node wherever needed
    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    # function to insert right node of the Binary Tree class
    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    # returns right child
    def getRightChild(self):
        return self.rightChild

    # returns left child
    def getLeftChild(self):
        return self.leftChild

    # sets the root value
    def setRootVal(self, obj):
        self.key = obj

    # returns the root value
    def getRootVal(self):
        return self.key

    # str method to return string for the tree that was made
    def __str__(self):
        s = f"{self.key}"
        s += '('
        if self.leftChild != None:
            s += str(self.leftChild)
        s += ')('
        if self.rightChild != None:
            s += str(self.rightChild)
        s += ')'
        return s


# class ExpTree which inherits from BinaryTree class
class ExpTree(BinaryTree):

    def make_tree(postfix):
        op_stack = Stack()
        # for loop iterates through infix equation
        for i in postfix:
            # checks if the operator is in valid operators
            if i in ['+', '-', '*', '/', '^']:
                right_child = op_stack.pop()
                left_child = op_stack.pop()
                op_tree = ExpTree(i)
                op_tree.leftChild = left_child
                op_tree.rightChild = right_child
                op_stack.push(op_tree)
            else:
                op_stack.push(ExpTree(i))

        return op_stack.pop()

    # for preorder traversal of the tree
    def preorder(tree):
        s = ''
        if tree != None:
            s = tree.getRootVal()
            s += ExpTree.preorder(tree.getLeftChild())
            s += ExpTree.preorder(tree.getRightChild())
        return s

    # for inorder traversal of the tree

    def inorder(tree):
        if tree is None:
            return ''
        elif tree.getLeftChild() is None and tree.getRightChild() is None:
            return str(tree.getRootVal())
        else:
            left_str = ExpTree.inorder(tree.getLeftChild())
            right_str = ExpTree.inorder(tree.getRightChild())
            return f'({left_str}{tree.getRootVal()}{right_str})'

    # for postorder traversal of the tree

    def postorder(tree):
        s = ''
        if tree:
            s += ExpTree.postorder(tree.getLeftChild())
            s += ExpTree.postorder(tree.getRightChild())
            s += str(tree.getRootVal())
        return s

    # evaluates the equation

    def evaluate(tree):
        if tree is None:
            return 0.0
        elif tree.leftChild is None and tree.rightChild is None:
            return float(tree.getRootVal())
        else:
            op = tree.getRootVal()
            left_val = ExpTree.evaluate(tree.getLeftChild())
            right_val = ExpTree.evaluate(tree.getRightChild())
            if op == '+':
                return left_val + right_val
            elif op == '-':
                return left_val - right_val
            elif op == '*':
                return left_val * right_val
            elif op == '/':
                return left_val / right_val
            elif op == '^':
                return left_val ** right_val

    def __str__(self):
        return ExpTree.inorder(self)


# a driver for testing BinaryTree and ExpTree
if __name__ == '__main__':
    # test a BinaryTree

    r = BinaryTree('a')
    assert r.getRootVal() == 'a'
    assert r.getLeftChild() == None
    assert r.getRightChild() == None
    assert str(r) == 'a()()'

    r.insertLeft('b')
    assert r.getLeftChild().getRootVal() == 'b'
    assert str(r) == 'a(b()())()'

    r.insertRight('c')
    assert r.getRightChild().getRootVal() == 'c'
    assert str(r) == 'a(b()())(c()())'

    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    assert str(r) == 'a(b(d()())(e()()))(c(f()())())'

    assert str(r.getRightChild()) == 'c(f()())()'
    assert r.getRightChild().getLeftChild().getRootVal() == 'f'

    # test an ExpTree

    postfix = '5 2 3 * +'.split()
    tree = ExpTree.make_tree(postfix)

    assert str(tree) == '(5+(2*3))'
    assert ExpTree.inorder(tree) == '(5+(2*3))'
    assert ExpTree.postorder(tree) == '523*+'
    assert ExpTree.preorder(tree) == '+5*23'
    assert ExpTree.evaluate(tree) == 11.0

    postfix = '5 2 + 3 *'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '((5+2)*3)'
    assert ExpTree.inorder(tree) == '((5+2)*3)'
    assert ExpTree.postorder(tree) == '52+3*'
    assert ExpTree.preorder(tree) == '*+523'
    assert ExpTree.evaluate(tree) == 21.0
