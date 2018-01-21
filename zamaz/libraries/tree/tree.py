"""tree module"""

import math

class ReprNode(object):
    def __init__(self, node, position):
        self._node = node
        self._position = position

    @property
    def position(self):
        '''getter for position'''
        return self._position

    @position.setter
    def position(self, value):
        '''setter for position'''
        self._position = value

    @property
    def node(self):
        '''getter for node'''
        return self._node


    def __repr__(self):
        return "({},{})".format(self._node.data, self._position)

class Node(object):
    """Node of tree, can have multiple children"""
    def __init__(self, parent, value, fixed_size=0):
        self._parent = parent
        self._data = value
        self._edges = []
        self._fixed_size = fixed_size
        self._children = [None] * fixed_size

    def insert_at(self, index, value):
        """inserts a node which takes this node as a parent"""
        if index >= len(self._children):
            self._children += ([None] * (index + 1 - len(self._children)))
        self._children[index] = Node(self, value, self._fixed_size)

    def get_at(self, index):
        """gets a child node specified by index"""
        if index >= len(self._children):
            raise "index too big"
        return self._children[index]

    @property
    def parent(self):
        '''getter for parent'''
        return self._parent

    @parent.setter
    def parent(self, value):
        '''setter for parent'''
        self._parent = value


    @property
    def data(self):
        '''getter for data'''
        return self._data

    @data.setter
    def data(self, value):
        '''setter for data'''
        self._data = value

    @property
    def children(self):
        '''getter for nodes'''
        return self._children

    @children.setter
    def children(self, value):
        '''setter for nodes'''
        self._children = value

    @property
    def children_datas(self):
        '''getter for children_datas'''
        return [child.data for child in self._children]

    @children_datas.setter
    def children_datas(self, values):
        '''setter for children_datas'''
        self._children = [Node(self, data, self._fixed_size) for data in values]

    @property
    def edges(self):
        '''getter for edges'''
        return self._edges


    def nb_notnull_children(self):
        """return number of not null children"""
        return len([child for child in self._children if child is not None])

    def __repr__(self):
        return str(self.data)

    def print_tree(self):
        tree_stack = []
        max_children = self.print_tree_recursive(0, 0, tree_stack)
        lines = ""
        for id_level, level in enumerate(tree_stack):
            spacing = max_children**(len(tree_stack) - id_level)
            line = ""
            line_before_before = ""
            line_before = ""
            for elt in level:
                if id_level == 0:
                    elt.node.position = spacing/2 + 10
                    line = " " * elt.node.position + "{}".format(elt.node.data)
                else:
                    parent_offset = elt.node.parent.position + spacing * elt.position
                    elt.node.position = parent_offset
                    offset = parent_offset - len(line)
                    line += (" "*offset + "{}".format(elt.node.data))
                    if elt.position < 0:
                        connector = "/"
                    elif elt.position > 0:
                        connector = "\\"
                    else:
                        connector = "|"
                    line_before_before += (" "*offset + "_")
                    line_before += (" "*offset + connector)

            lines += (line_before + "\n" + line + "\n")
        return lines

    def print_tree_recursive(self, level, position, tree_stack):
        """creates a list of lines containing all tree elements by level"""
        myself = ReprNode(self, position)
        if self.nb_notnull_children() == 0:
            if level >= len(tree_stack):
                tree_stack.append([myself])
            else:
                tree_stack[level].append(myself)
            return 1
        else:
            if level >= len(tree_stack):
                tree_stack.append([myself])
            else:
                tree_stack[level].append(myself)

            children_len = len(self._children)
            max_line_len = children_len
            for idx, child in enumerate(self._children):
                if child is None:
                    continue
                max_ch_line_len = child.print_tree_recursive(level + 1,
                                                             idx - children_len/2, tree_stack)
                max_line_len = max(max_ch_line_len, max_line_len)

            return max_line_len

    def compute_edges(self):
        self._edges = []
        self.compute_edges_recursive(self._edges)

    def compute_edges_recursive(self, edges):
        """computes edges from tree"""
        for child in self._children:
            if child is not None:
                edges.append((self, child))
                child.compute_edges_recursive(edges)

class Tree(object):
    """three object, stores the root node"""
    def __init__(self, *args, **kwargs):
        super(Tree, self).__init__()
        self._fixed_size = kwargs['fixed_size']
        self._root = Node(None, args[0], fixed_size=self._fixed_size)

    def get_root(self):
        """returns root of tree"""
        return self._root

    def __repr__(self):
        return repr(self.get_root())
