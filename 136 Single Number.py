class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i=0
        while True:
            if len(nums)==1:
                break
            if i>len(nums)-1:
                i=0
            if i<-len(nums)+1:
                i=0
            else:
                try:
                    a=nums[i]
                    nums.remove(a)
                    nums.remove(a)
                    i=i+1
                except ValueError:
                    nums.append(a)
                    i=i-1
        return nums[0]
