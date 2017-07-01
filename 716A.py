n,c=map(int,raw_input().split())
w=map(int,raw_input().split())
x=0;arr=[0]
if len(w)==1:
  print 1
  exit()
for i in w:
  arr.append(i)
for i in range(1,n):
  if arr[i+1]-w[i-1]<=c:
    x+=1
  else:
    x=1
print x