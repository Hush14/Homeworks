def deliteli(x):
    a=[]
    i=1
    while x>=i:
        if x%i==0:
            a.append(i)
        i+=1
    return a

print(deliteli(int(input())))

