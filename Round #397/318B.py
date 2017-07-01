counter=0
ans=0
for i in raw_input().split('heavy'):
    ans+=i.count('metal')*counter
    counter+=1
print ans

