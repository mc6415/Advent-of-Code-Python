total = 0
with open('../../input/day2.txt') as f:
    for line in f:
        l, w, h = (int(n) for n in line.split('x'))
        total += l*w*h
        total += 2*(l + w + h - max(l, w, h))
print "Ribbon needed: " + str(total)