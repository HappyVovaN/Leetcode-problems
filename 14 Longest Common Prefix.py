class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l2=[]
        for i in range(0,len(strs)):
            l2.append(len(strs[i]))
        try:
            min_len=min(l2)
        except:
            return ''
            
        m=-1 
        for j in range(0,min_len):
            n=1
            for i in range(0,len(strs)-1):
                if strs[i][m+1]==strs[i+1][m+1]:
                    n=n*1
                else:
                    n=n*0
            if n==1:
                m=m+1
            if n==0:
                break
        answer = strs[0][:m+1]
        if m==-1:
            return ''
        else :
            return answer
