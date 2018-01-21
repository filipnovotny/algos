import re

s1 = "Mayer is a very common Name"
s2 = "He is called Meyer but he isn't German."
s = s2 + "\n" + s1
print(re.search(r"^M[ae][iy]er", s))
print(re.search(r"^M[ae][iy]er", s, re.MULTILINE))
