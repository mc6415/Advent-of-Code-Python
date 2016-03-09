evalLen = 0
lineLen = 0

with open("../../input/day8.txt") as f:
    for line in f:
        evalLen += len(eval(line))
        lineLen += len(line.strip())
        
print lineLen - evalLen