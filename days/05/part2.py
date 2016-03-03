import re

g1 = re.compile("([a-z][a-z]).*\\1")
g2 = re.compile("([a-z])[a-z]\\1")

with open('../../input/day5.txt') as f:
    print len([l for l in f if g1.search(l) and g2.search(l)])