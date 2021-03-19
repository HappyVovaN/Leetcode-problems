class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=='':
            return 0
        j=0
        z=[]
        len1=len(haystack)
        len2=len(needle)
        while True:
           
                if j>len1:
                    return -1
                if haystack[j:j+len2]!=needle:
                    j=j+1
                    print(j)

                else:
                    return j
                    break
            
