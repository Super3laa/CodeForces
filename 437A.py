a = [len(map(str,raw_input()[2::])), 'A']
b = [len(map(str,raw_input()[2::]), 'B')]
c = [len(map(str,raw_input()[2::]), 'C')]
d = [len(map(str,raw_input()[2::]), 'D')]

o = list(sorted([a,b,c,d]))
print o 

if  o[0]<= o[1]/2 and o[0]<= o[2]/2 and o[0]<= o[3]/2:
    print o[0][1]
elif o[1]<= o[0]/2 and o[1]<= o[2]/2 and o[1]<= o[3]/2:
    print o[1][1]
elif o[3]<= p[0]/2 and o[3]<= o[2]/2 and o[3]<= o[2]/2:
    print o[3][1]
else:
    print'C'



