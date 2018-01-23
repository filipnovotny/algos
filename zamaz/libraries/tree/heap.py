import math
from binary_tree import BinaryTree, BinaryNode

class Heap(object):
    """implements a heap"""
    def __init__(self):
        # the heap is a particular binary tree which is constructed left-to right
        # for that reason we can easily store the data in an array which would not
        # be possible with a general purpose tree
        self._data = []
        self._element_to_index = dict() #search is better than O(k)

    @property
    def top(self):
        '''getter for top'''
        return self._data[0]
    

    def _swap(self, idx1, idx2):
        self._element_to_index[self._data[idx1]],self._element_to_index[self._data[idx2]]  = idx2, idx1
        self._data[idx1], self._data[idx2] = self._data[idx2], self._data[idx1]


    def _bubble_up(self, idx):
        """reorganize tree to satisfy heap properties"""
        raise NotImplementedError

    def _bubble_down(self, idx):
        """reorganize tree to satisfy heap properties"""
        raise NotImplementedError

    def insert(self, data):
        """ inserts into heap"""
        self._data.append(data)
        self._element_to_index[data] = len(self._data)-1
        self._bubble_up(len(self._data) - 1)

    def remove(self):
        """ remove from heap"""
        self._data[0] = self._data.pop()
        self._bubble_down(0)

    def remove_el(self, elt):
        """ remove specific element from heap O(n) because of the search"""
        idx = self._element_to_index[elt]
        del self._element_to_index[elt]
        if idx is not None:
            self._data[idx] = self._data.pop()
            self._element_to_index[self._data[idx]] = idx
            new_idx = self._bubble_down(idx)


    def left_index(self, index):
        """return index of left child"""
        return index * 2 + 1

    def right_index(self, index):
        """return index of right child"""
        return index * 2 + 2

    def parent_index(self, index):
        """return index of parent"""
        return (index-1) // 2


    def left(self, index):
        """returns left child"""
        if self.left_index(index) >= len(self._data):
            return None
        else:
            return self._data[self.left_index(index)]

    def right(self, index):
        """returns right child"""
        if self.right_index(index) >= len(self._data):
            return None
        else:
            return self._data[self.right_index(index)]

    def parent(self, index):
        """returns parent of node"""
        if self.parent_index(index) < 0:
            return None
        else:
            return self._data[self.parent_index(index)]

    def debug(self):
        print(self._data)
        print(self._element_to_index)

    def __repr__(self):
        index = 0
        max_level = int(math.log(len(self._data) + 1, 2))+1
        lines = ""
        for level in range(0, max_level):
            spacing = (2 ** (max_level - level))
            line = ""
            line_before = ""
            index = 2**level - 1
            while index < len(self._data) and index < (2**(level+1))-1:
                line += (" " * spacing) + str(self._data[index])
                if index % 2 == 1:
                    line_before += (" " * spacing) + "/"
                    line_before += (" " * (spacing))
                    line += (" " * (spacing-(len(str(self._data[index])))))
                else:
                    line_before += (" " * spacing) + "\\"
                index +=1

            lines += line_before
            lines += "\n"
            lines += line
            lines += "\n"

        return lines
