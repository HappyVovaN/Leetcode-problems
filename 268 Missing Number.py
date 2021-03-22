class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i=0
        while True:
            try:
                nums.remove(i)
                i=i+1
            except ValueError:
                return i
