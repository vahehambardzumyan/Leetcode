class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d={}
        for elem in nums:
            if not d.get(elem):
                d[elem]=1
            else:
                d[elem]= d.get(elem)+1
     

        return any([(value>1)for value in d.values()])
   
        