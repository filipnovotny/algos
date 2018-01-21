from itertools import product, permutations, combinations, combinations_with_replacement

l = [1,5,8,45]
m = [-1,-8,-2,-3]

print(list(product(l,repeat=2)))
print(list(product(l,repeat=3)))
print("------")
print(list(product(l,m)))
print(list(combinations(l,2)))
print(list(permutations(l,2)))
print(list(combinations_with_replacement(l,2)))
