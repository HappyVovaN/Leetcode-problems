class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        num1=0
        for i in range(0,len(A)):
            num1=num1+A[i]*10**(len(A)-i-1)

        num3=num1+K
        num3_str=str(num3) 
        num3_list=list(num3_str)
        return num3_list 
