class convert(int):
    def ArabRoman(self, num):
        arab = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        rom = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        rnum = ''
        i = 0
        while num > 0:
            for j in range(num // arab[i]):
                rnum += rom[i]
                num -= arab[i]
            i += 1
        return rnum

    def RomanArab(self, num):
        rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        arnum = 0
        for i in range(len(num)):
            if i > 0 and rom[num[i]] > rom[num[i - 1]]:
                arnum += rom[num[i]] - 2 * rom[num[i - 1]]
            else:
                arnum += rom[num[i]]
        return arnum

num=input()
ifint=num.isnumeric()

if ifint:
    print(convert().ArabRoman(int(num)))
else:
    print(convert().RomanArab(num))