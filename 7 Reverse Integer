class Solution:
    def reverse(self, x: int) -> int:
        y=list(str(x))
        print(len(y))
        number=0
        b=1
        if y[0]=='-':
            y.remove('-')
            b=-1
        for i in range(0, len(y)):
             print(y[i])
             number=number+(int(y[i]))*(10**(i))
        if number>2**31:
            number=0
        return number*b
