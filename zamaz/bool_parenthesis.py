try:
    import networkx as nx
except:
    pass
import matplotlib.pyplot as plt
from libraries.tree.drawable_tree import DrawableTree
from libraries.tree.binary_tree import BinaryTree, BinaryNode
from copy import deepcopy

symbols = ['|','&','^','^',"&"]
statements = ['T', 'T', 'F', 'T','T','F']


class SymbolTree(object):
    """three object, stores the root node"""
    def __init__(self, *args, **kwargs):
        super(SymbolTree, self).__init__()
        self._root = BinaryNode(None, args[0])

    def get_root(self):
        """returns root of tree"""
        return self._root

    def __repr__(self):
        return repr(self.get_root())

class SymbolNode(BinaryNode):
    def __init__(self, parent, value, order):
        super(SymbolNode, self).__init__(parent, value)

        self._order = order

    @property
    def order(self):
        '''getter for order'''
        return self._order

    def attach_next_symbol(self, trees=[]):
        node_parent = deepcopy(self)
        node_right = deepcopy(self)
        node_left = deepcopy(self)

        if self.order < len(symbols)-1:
            node_parent.parent = SymbolNode(None, symbols[node_parent.order+1], node_parent.order+1)
            node_parent.parent.left = node_parent
            node_parent = node_parent.parent

            node_right.right = SymbolNode(node_right, symbols[self.order+1], self.order+1)
            node_left.left = SymbolNode(node_left, symbols[self.order+1], self.order+1)
        if self.order == 0 and self._order < len(symbols)-1:
            node_parent.attach_next_symbol(trees)
            node_right.right.attach_next_symbol(trees)
        elif self.order > 0 and self._order < len(symbols)-1:
            if self.parent is None: # I am the parent
                node_parent.attach_next_symbol(trees)
                node_right.right.attach_next_symbol(trees)
            else:
                node_right.right.attach_next_symbol(trees)
                node_left.left.attach_next_symbol(trees)
        elif self.order == len(symbols)-1:
            if self.parent is None:
                trees.append(self)
            else:
                node = self
                while node.parent is not None:
                    node = node.parent

                trees.append(node)

    def attach_statements(self, sorder):
        if self.left is None:
            self.left = SymbolNode(self, statements[sorder], sorder)
            sorder+=1
        else:
            sorder = self.left.attach_statements(sorder)

        if self.right is None:
            self.right = SymbolNode(self, statements[sorder], sorder)
            sorder+=1
        else:
            sorder = self.right.attach_statements(sorder)

        return sorder

    def evaluate(self):
        if self.data == "T":
            return True
        elif  self.data == "F":
            return False
        elif self.data == "&":
            return self.left.evaluate() and self.right.evaluate()
        elif self.data == "|":
            return self.left.evaluate() or self.right.evaluate()
        elif self.data == "^":
            return self.left.evaluate() != self.right.evaluate()

    def evaluate_lex(self):
        if self.data == "T":
            return "T"
        elif  self.data == "F":
            return "F"
        elif self.data == "&":
            return "(" + self.left.evaluate_lex() + " & " + self.right.evaluate_lex() + ")"
        elif self.data == "|":
            return "(" + self.left.evaluate_lex()  + " | " +  self.right.evaluate_lex() + ")"
        elif self.data == "^":
            return "(" + self.left.evaluate_lex()  + " ^ " +  self.right.evaluate_lex() + ")"


node = SymbolNode(None,symbols[0],0)
trees = []
node.attach_next_symbol(trees)
nb_true = 0
for tree in trees:
    tree.attach_statements(0)
    if tree.evaluate():
        nb_true += 1
    print("---------")
    print(tree.print_tree())
    print(tree.evaluate_lex())

print(nb_true)