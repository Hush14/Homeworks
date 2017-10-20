def zapolnenie(n):
    a = [[1]]
    for i in range(1, n):
        b = [1]
        for j in range(0, i-1):
            b.append(a[i-1][j]+a[i-1][j+1])
        b.append(1)
        a.append(b)
    return a

def triangle():
    height = int(input())
    for i in zapolnenie(height):
        print(" " * (height * 2), i)
        height -= 1
triangle()