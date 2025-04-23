class Solution:
    def romanToInt(self, s: str) -> int:
        di={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        res= 0
        prev = 0
        for elem in s[::-1]:
            curent  = di[elem]
            if curent >= prev:
                res += curent
            else:
                res -= curent
            prev = curent


        return res