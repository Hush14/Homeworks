import dlb

a = dlb.PositionalList()
print('Input integers: ')
s = input().split()
for i in s:
    a.add_last(int(i))
print('Input v: ')
v = int(input())

class nchisla:
    def __init__(self, first, second):
        self.first = first
        self.second = second


def poisk(v):
    s1 = a._header._next
    s2 = a._trailer._prev
    while s2!= s1:
        if s1._element + s2._element == v:
            return nchisla(s1._element, s2._element)
        if s1._element + s2._element > v:
            s2 = s2._prev
        if s1._element + s2._element < v:
            s1 = s1._next
    return None

l = poisk(v)

if l == None:
    print(l)
else:
    print(l.first, l.second)