def arithmetic(a,b,c):
    s=''
    if c=='+':
        s=a+b
    elif c=='-':
        s=a-b
    elif c=='*':
        s=a*b
    elif c=='/':
        if b!=0:
            s=a/b
        else:
            s='Невозможно выполнить операцию'
    return s
a=int(input())
b=int(input())
c=input()
print(arithmetic(a,b,c))