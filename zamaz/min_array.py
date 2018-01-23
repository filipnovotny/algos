from libraries.tree.min_heap import MinHeap


A = [1,3,0,5,6,7,2]

def find_min_array(A,k):
    B = []
    h = MinHeap()
    for i in range(0,len(A)):
        h.insert(A[i])
        if i>=k:
            h.remove_el(A[i-k])
        if i>=k-1:
            B.append(h.top)
    return B

print(find_min_array(A,4))
