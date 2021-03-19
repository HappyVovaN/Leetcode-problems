class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        while True:
            try:
                if nums[i]==nums[i+1]:
                    del nums[i+1]
                if nums[i]!=nums[i+1]:
                    i=i+1
            except IndexError:
                break
