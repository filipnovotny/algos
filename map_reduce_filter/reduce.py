import itertools
l = xrange(10)
accumulator_sum = reduce(lambda x,y: x+y,l)

print(accumulator_sum)

