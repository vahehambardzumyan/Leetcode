class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
       
        # for i in range(len(nums)):
        #     for j in range(1+i,len(nums)):
        #         if nums[i]>nums[j]:
        #             nums[i], nums[j]= nums[j], nums[i]
        left=0 
        right=len(nums)-1
        mid=0
        while mid <= right :
            if nums[mid]==0:
                nums[mid], nums[left]=nums[left], nums[mid]
                left+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid], nums[right]=nums[right], nums[mid]
                right-=1
               