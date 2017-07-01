import math
n=input()
distance=0;x=0;y=0
for i in range(n):
   z=map(int,raw_input().split())
   x=(z[4]-z[1])
   y=(z[5]-z[2])
   distance=math.sqrt(math.pow(x,2)+math.pow(y,2))
   Rf=z[3]
   Rr=z[0]
   if ((distance>= (Rf+Rr)) or(abs((Rf-Rr))<distance<(Rf+Rr))) or z[0]<z[3]:
     print 'Dead'
   else:
     print'Rich'