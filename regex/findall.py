import re
t="A fat cat doesn't eat oat but a rat eats bats."
mo = re.findall("[force]at", t)
print (mo)

items = items = re.findall("([0-9]+).*: (.*)", "Customer number: 232454, Date: February 12, 2011")
print items

p = re.compile("[a-z]")
for m in p.finditer('a1b2c3d4'):
    print m.span(), m.group()
