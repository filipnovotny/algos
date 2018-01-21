import heapq

l = [3,8,1,4,7,0]
n=len(l)
k=4
heap = heapq.heapify(l)


for i in range(0,n) :
    for j in range(i,k):
        min_heapq.heappop(heap)
min_list = [heapq.heappop(heap) for ]