from libraries.tree.binary_tree import BinaryTree,BinaryNode
from libraries.tree.drawable_tree import DrawableTree

def list_to_tree_recursive(node):
    list_left_tail = list_right_head = None
    if node.left is None and node.right is None:
        return node,node
    if node.left is not None:
        list_left_head,list_left_tail = list_to_tree_recursive(node.left)
        list_left_tail.right = node
        node.left = list_left_tail

    if node.right is not None:
        list_right_head,list_right_tail = list_to_tree_recursive(node.right)
        list_right_head.left = node
        node.right = list_right_head

    return list_left_tail, list_right_head

def print_tree_recursive(node):
    node1 = node2 = []
    if node.left is None and node.right is None:
        return [node.data]

    if node.left is not None:
        node1 = print_tree_recursive(node.left)

    if node.right is not None:
        node2 = print_tree_recursive(node.right)

    return node1 + [node] + node2



bsase = node = BinaryNode(None,10)
node.left = BinaryNode(node.left,12)
node.right = BinaryNode(node.right,15)
hd = node.left.left = BinaryNode(node.left.left,25)
node.left.right = BinaryNode(node.left.right,30)
node.right.left = BinaryNode(node.right.left,36)

print(print_tree_recursive(bsase))
list_to_tree_recursive(node)

node = hd
while node is not None:
    print(node.data)
    node = node.right


# class MyTree(BinaryTree, DrawableTree):
#     def __init__(self, *args, **kwargs):
#         super(MyTree, self).__init__(*args, **kwargs)


# try:
#     import networkx as nx
# except:
#     pass
# import matplotlib.pyplot as plt

# tree = MyTree(node)
# tree.nodes_to_graph()
# nx.draw(tree.graph, pos=tree.pos, with_labels=True)
# plt.show()
