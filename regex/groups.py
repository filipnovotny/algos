import re

s="Customer number: 232454, Date: February 12, 2011"
mo = re.search("([0-9]+).*: (.*)", s)
v = mo.group()
print(v)
print(mo.group(1))
print(mo.group(2))
mo = re.search("(?P<match1>[0-9]+).*: (?P<match2>.*)", s)
print(mo.group())
print(mo.group("match1"))
print(mo.group("match2"))
print (mo.span("match2"))
start,end = mo.span("match1")
res = s[:start]+"lol"+s[end:]
print(res)