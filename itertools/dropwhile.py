from itertools import dropwhile

data = [1,4,6,2,34,9]
x = dropwhile(lambda x: x<10,data)
y = filter(lambda x: x>=10,data)
z = dropwhile(lambda x: x<10,data)

print(list(x))
print(y)
print(list(z))