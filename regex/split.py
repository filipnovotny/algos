import re
metamorphoses = "OF bodies chang'd to various forms, I sing: Ye Gods, from whom these miracles did spring, Inspire my numbers with coelestial heat;"
ret = re.split("\W+",metamorphoses)
print(ret)
