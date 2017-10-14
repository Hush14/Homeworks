x=int(input())
a=[]
i=1
while x>=i:
    if x%i==0:
        a.append(i)
    i+=1
print(*a)

