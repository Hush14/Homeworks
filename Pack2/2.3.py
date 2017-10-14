def fact(n):
    fac = 1
    i = 0
    while i < n:
        i += 1
        fac = fac * i
    return fac

def C(n,k):
    return round(fact(n) / (fact(k) * fact(n-k)))


def triangle(n):
    for i in range(n):
        s = ""
        for j in range(i+1):
            s = s + str(C(i,j)) + "\t"
        print(s)

x=int(input())
triangle(x)