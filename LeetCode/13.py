class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        rn= {'I' : 1,'V': 5,'X': 10,'L' : 50,'C' : 100,'D' : 500,'M': 1000}
        prev = 1001
        for i in s:
            if prev < rn[i]:
                num -= 2*prev
                num += rn[i]
            else:
                num += rn[i]
            prev = rn[i]
        return num
