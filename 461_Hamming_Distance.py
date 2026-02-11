class Solution(object):
    def hammingDistance(self, x, y):
        res = [ 1 for i in str(bin(x ^ y)) if  i=='1']
        return sum(res)