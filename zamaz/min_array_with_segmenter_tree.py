from libraries.tree.max_heap import MaxHeap
from libraries.tree.segment_tree import list_to_tree
import sys

def find_interval_min(node, start, end):
    if start <= node.data.start and node.data.end <= end: #complete overlap
        return node.data.val
    elif start > node.data.end or end < node.data.start:
        return sys.maxint
    else:
        return min(find_interval_min(node.left,start,end),find_interval_min(node.right,start,end))

l = [1,3,0,5,6,7,2]
tree = list_to_tree(l)

B = []
k=4
for i in range(0,len(l)-k+1):
    B.append(find_interval_min(tree, i, i+k))

print(B)