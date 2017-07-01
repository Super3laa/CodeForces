m, s =map(int, raw_input().split())
if(m==1 and s==0):
    print '0 0'
elif(9*m < s or s == 0):
    print '-1 -1'
else:
    x = 10**(m-1)
    for i in range(s-1):
        x += 10**(i/9)
    y = 0
    for i in range(s):
        y+=10**(m-1-i/9)
    print x,y
