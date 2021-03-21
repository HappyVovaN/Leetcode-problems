class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        slist=s.split()
        print(slist)
        if slist==[]:
            return 0
        else:
            return len(slist[-1])
