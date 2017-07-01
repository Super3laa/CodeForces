from operator import sub
n=float(input())
s=[];A=[];B=[]
for i in range(int(n)):
  s.append(n/(i+1))
for a,b in enumerate(s):
  if a+1<=b and ((a+1)*int(b))==n:
    A.append((a+1))
    B.append((int(b)))
    
g= map(sub,B,A).index(min(map(sub,B,A)))
print A[g],B[g]
