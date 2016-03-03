floor = 0
with open('../../input/day1.txt') as f:
    # Loop other the input, adding and subtracting as needed, break on floor < 0
    for i, char in enumerate(f.read(), 1):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        if floor < 0:
            break;
print "Enters basement at step: " + str(i)