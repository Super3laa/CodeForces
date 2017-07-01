n = int(input())
arr=sorted(map(int,raw_input().split()))
ans=[arr[i+1]-arr[i] for i in range(n-1)]
print min(ans),ans.count(min(ans))
