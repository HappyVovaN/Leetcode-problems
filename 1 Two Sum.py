
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Definitely_not=[]
        nums1=nums
        result=[0,0]

        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    result[0]=i
                    result[1]=j
                else:
            
                    1
        return result        
                      
    
