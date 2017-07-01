n = int(input())
arr = map(int, raw_input().split())
print max(n-arr.count(min(arr))-arr.count(max(arr)),0)
