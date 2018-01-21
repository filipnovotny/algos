from itertools import compress

ret  = compress([1,2,3,4],[0,0,1,0])
print(list(ret))