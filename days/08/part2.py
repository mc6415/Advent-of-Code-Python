totalLen = 0

with open("../../input/day8.txt") as f:
    for line in f:
        totalLen += line.strip().count('\\') + line.strip().count('"') + 2
print totalLen