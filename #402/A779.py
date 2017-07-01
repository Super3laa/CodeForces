n = int(input())
A = map(int, raw_input().split())
B = map(int, raw_input().split())
if sorted(A)==sorted(B):
    print 0
    exit()
for i in A:
    if i in B:
        B.remove(i)
print (len(B)/2 if len(B)/2!=0 else -1)
