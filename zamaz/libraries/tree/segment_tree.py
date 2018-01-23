from binary_tree import BinaryNode, BinaryTree
from drawable_tree import DrawableTree

class SegmentData(object):
    def __init__(self, start, end, val):
        self._start = start
        self._end = end
        self._val = val

    @property
    def start(self):
        '''getter for start'''
        return self._start

    @property
    def end(self):
        '''getter for end'''
        return self._end

    @property
    def size(self):
        '''getter for size'''
        return self.end - self.start

    @property
    def val(self):
        '''getter for val'''
        return self._val

    @val.setter
    def val(self, value):
        '''setter for val'''
        self._val = value



    def __repr__(self):
        return "[{};{}]={}".format(self.start, self.end, self.val)


def list_to_tree_recursive(l, node):
    if node.data.end - node.data.start == 0:
        node.data = SegmentData(node.data.start,node.data.end, l[node.data.start])
    else:
        data_left   = SegmentData(node.data.start,node.data.start + node.data.size//2, None)
        data_right  = SegmentData(node.data.start + node.data.size//2 + 1, node.data.end, None)
        node.left   = BinaryNode(node, data_left )
        node.right  = BinaryNode(node, data_right )
        list_to_tree_recursive(l, node.left)
        list_to_tree_recursive(l, node.right)
        node.data.val = min(node.left.data.val,node.right.data.val)

def list_to_tree(l):
    seg = SegmentData(0,len(l)-1, None)
    node = BinaryNode(None, seg)
    list_to_tree_recursive(l, node)
    return node



if __name__ == "__main__":
    class MyTree(BinaryTree, DrawableTree):
        def __init__(self, *args, **kwargs):
            super(MyTree, self).__init__(*args, **kwargs)

    parent = list_to_tree([1,3,0,5,6,7,2])

    from tree import Tree
    try:
        import networkx as nx
    except:
        pass
    import matplotlib.pyplot as plt

    tree = MyTree(parent)
    tree.nodes_to_graph()
    nx.draw(tree.graph, pos=tree.pos, with_labels=True)
    plt.show()
