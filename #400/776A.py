p1, p2 = raw_input().split()
print p1, p2
for i in range(int(input())):
    s1, s2 = raw_input().split()
    if s1 == p1 or s1 == p2:
        if s1 == p1:
            p1 = s2
            print p1, p2
        if s1 == p2:
            p2 = s2
            print p1, p2
