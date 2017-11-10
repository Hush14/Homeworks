def deri(f):
    st = ''

    def derivative(b):
        if 'x' not in b:
            d = ''
        else:
            a = b.split('x')
            if a[1] == '':
                d = a[0]
            elif a[1] == '^2':
                d = a[0] + 'x'
            else:
                d = str(int(a[0])*int(a[1][1:])) + 'x^' + str(int(a[1][1:])-1)
                if a[0][0] != '-':
                    d = '+' + d
        return d

    def splitt(f):
        sign = f.split('+')
        k = []
        for j in sign:
            k.append(j.split('-'))
        m = []
        for a in k:
            for i in range(len(a)):
                if i > 0:
                    m.append('-' + a[i])
                else:
                    m.append('+' + a[i])
            pass

        return m

    skra = splitt(f)
    for i in skra:
        st += derivative(i)

    return st if st[0] != '+' else st[1:]

print('Enter polynomial:')
s=str(input())
print(deri(s))
