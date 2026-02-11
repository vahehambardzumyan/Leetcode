class Solution(object):
    def lengthOfLastWord(self, s):
        count = 0
        for i in s[::-1]:
            if i == ' ' and count==0:
                continue
            if i == ' ' and count!=0:
                break
            count+=1
        return count