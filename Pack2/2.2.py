x=int(input())
i=1
sum=0
while x>i:
    if x%i==0:
        sum=sum+i
    i+=1
if x==sum:
    print('perfect')
else:
    print('not perfect')