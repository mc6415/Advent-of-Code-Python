total = 0
with open('../../input/day2.txt') as f:
    for line in f:
        # Store length, width and height
        l, w, h = (int(n) for n in line.split('x'))
        # Calculate area of each side
        al, aw, ah = l*w, w*h, l*h
        # Add smallest area for the slack
        total += min(al,aw,ah)
        total += 2 * (al + aw + ah)
        
print "Wrapping paper needed: " + str(total)