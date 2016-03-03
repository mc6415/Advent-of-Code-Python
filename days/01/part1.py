f = open('../../input/day1.txt', 'r')
print "Floor: " + str(sum(1 if x == '(' else -1
         for x in f.read().strip()))
