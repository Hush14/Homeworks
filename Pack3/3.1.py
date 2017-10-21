class par:
   def valid(self, s):
        a = []
        skobki = {"(": ")", "{": "}", "[": "]"}
        for i in s:
            if i in skobki:
                a.append(i)
            elif len(a) == 0 or skobki[a.pop()]!= i:
                return False
        return len(a) == 0

s=str(input())
print(par().valid(s))