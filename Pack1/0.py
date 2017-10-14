a=list(input().split())
sdvig=int(input())
while sdvig>0:
    a.insert(0, a.pop())
    sdvig=sdvig-1
print(*a)





