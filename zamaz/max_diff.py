from libraries.tree.binary_tree import BinaryTree,BinaryNode
from libraries.tree.drawable_tree import DrawableTree
import sys

def max_diff(node):
    min_right = min_left = None
    max_diff_left = max_diff_right = None
    if node.left is None and node.right is None:
        node.deco = node.data
        return node.data, -sys.maxint - 1

    if node.left is not None:
        min_left, max_diff_left = max_diff(node.left)

    if node.right is not None:
        min_right, max_diff_right = max_diff(node.right)

    if min_left is None:
        min_val_up_to_me = min_right
        max_diff_up_to_me = max_diff_right
    elif min_right is None:
        min_val_up_to_me = min_left
        max_diff_up_to_me = max_diff_left
    else:
        min_val_up_to_me = min(min_right, min_left)
        max_diff_up_to_me = max(max_diff_left,max_diff_right)

    node.deco = max(node.data - min_val_up_to_me,max_diff_up_to_me)
    return min_val_up_to_me, max(node.data - min_val_up_to_me,max_diff_up_to_me)

node = BinaryNode(None,5)
node.left = BinaryNode(node.left,60)
node.right = BinaryNode(node.right,2)
node.left.left = BinaryNode(node.left.left,28)
node.left.right = BinaryNode(node.left.right,3)
node.right.left = BinaryNode(node.right.left,50)
node.right.left.left = BinaryNode(node.right.left,1)
node.right.left.right = BinaryNode(node.right.left,88)


max_diff(node)
print(node.deco)
# print(node.print_tree())

class MyTree(BinaryTree, DrawableTree):
    def __init__(self, *args, **kwargs):
        super(MyTree, self).__init__(*args, **kwargs)


try:
    import networkx as nx
except:
    pass
import matplotlib.pyplot as plt

tree = MyTree(node)
tree.nodes_to_graph()
nx.draw(tree.graph, pos=tree.pos, with_labels=True)
plt.show()
