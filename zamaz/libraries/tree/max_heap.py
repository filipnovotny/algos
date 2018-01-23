from heap import Heap

class MaxHeap(Heap):
    """Min Heap class"""
    def _bubble_up(self, idx):
        """reorganize tree to satisfy heap properties"""
        child_index = idx

        #if child is smaller than parent
        while self.parent(child_index) is not None and self._data[child_index] > self.parent(child_index):
            parent_index = self.parent_index(child_index)
            self._swap(child_index,parent_index)
            child_index = parent_index

        return child_index

    def _bubble_down(self, idx):
        """reorganize tree to satisfy heap properties"""
        parent_idx = idx
        #if child is smaller than parent
        while True:
            if self.left(parent_idx) is None and self.right(parent_idx) is None:
                break;
            elif self.left(parent_idx) is None:
                smallest_idx = self.right_index(parent_idx)
            elif self.right(parent_idx) is None:
                smallest_idx = self.left_index(parent_idx)
            else:
                if self.left(parent_idx) > self.right(parent_idx):
                    smallest_idx = self.left_index(parent_idx)
                else:
                    smallest_idx = self.right_index(parent_idx)

            if self._data[smallest_idx] > self._data[parent_idx]:
                self._swap(smallest_idx, parent_idx)
                parent_idx = smallest_idx
            else:
                break;

        return parent_idx
