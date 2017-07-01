n,m = map(int, raw_input().split())
arr=[]
for i in range (n):
  arr.append(0)
for i in range(m):
  z=map(int,raw_input().split())
  arr[z.index(max(z))]=arr[z.index(max(z))]+1
print arr.index(max(arr))+1