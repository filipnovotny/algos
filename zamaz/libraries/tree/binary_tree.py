from tree import Tree, Node

class BinaryNode(Node):
    """Node of tree, can have 2 children"""
    def __init__(self, parent, value):
        super(BinaryNode, self).__init__(parent, value, fixed_size=2)

        self._left = self._children[0]
        self._right = self._children[1]

    @property
    def left(self):
        '''getter for left'''
        return self._left

    @left.setter
    def left(self, value):
        '''setter for left'''
        self._left = value
        self._children[0] = self._left

    @property
    def right(self):
        '''getter for right'''
        return self._right

    @right.setter
    def right(self, value):
        '''setter for right'''
        self._right = value
        self._children[1] = self._right



class BinaryTree(object):
    """three object, stores the root node"""
    def __init__(self, *args, **kwargs):
        super(BinaryTree, self).__init__()
        self._root = BinaryNode(None, args[0])

    def get_root(self):
        """returns root of tree"""
        return self._root

    def __repr__(self):
        return repr(self.get_root())
