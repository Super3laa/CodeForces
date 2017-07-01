x = input()
numbers = []
numbers = raw_input().split(' ')
numbers = map(int,numbers)
E=[]
O=[]
for i in numbers :
    if i %2 <> 0:
        E.append(numbers.index(i)+1)
    if i%2== 0:
        O.append(numbers.index(i)+1)
if len(E)>len(O):
     print O[0]
else:
        print E[0]