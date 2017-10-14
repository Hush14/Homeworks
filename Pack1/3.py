x=int(input())
a=[]
k=0
i=1
while x>=i:
    if x%i==0:
        k+=1
    i+=1
if k==2:
    print('prime')
else:
    print('not prime')