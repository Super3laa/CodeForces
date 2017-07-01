n = int(input())
T=0;D=0;z=0
arr=map(int,raw_input().split())
for i in sorted(arr):
  if T <= i:
    D+=1
    T=i+T
print D