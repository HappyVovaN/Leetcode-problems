class Solution:
    def romanToInt(self, s: str) -> int:
        z=list(s)
        print(z)
        z1=[]
        for i in range(0, len(z)):
            if z[i]=='I':
                z1.append(1)
            if z[i]=='V':
                z1.append(5)
            if z[i]=='X':
                z1.append(10)
            if z[i]=='L':
                z1.append(50)
            if z[i]=='C':
                z1.append(100)
            if z[i]=='D':
                z1.append(500)
            if z[i]=='M':
                z1.append(1000)
        print(z1)
        for i in range(0, len(z1)-1):
            if z1[i]<z1[i+1]:
                z1[i]=-z1[i]
        print(z1)
        z2=sum(z1)
        print(z2)
        return z2
            
