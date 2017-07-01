n = int(input())
w= raw_input()
w= w.split(' ')
w = list(w)
one = []
two = []
for i in  w:
    if i == '200':
        two.append(i)
    elif i== '100':
        one.append(i)
if len(one) % 2==1 or(len(two)%2==1 and len(one) == 0):
    print'NO'
else:
    print'YES'
