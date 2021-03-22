class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number1=0
        for i in range(0,len(digits)):
            number1=number1+digits[i]*10**(len(digits)-i-1)
        number2=number1+1
        number2_str=str(number2)            
        number2_list=list(number2_str)
        for i in range(0,len(number2_list)):
            number2_list[i]=int(number2_list[i])
        return number2_list        
        
