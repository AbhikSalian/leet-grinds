class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sin=0
        tin=0
        n=len(t)
        while tin<n:
            if sin==len(s):
                return True
            if t[tin]==s[sin]:
                tin+=1
                sin+=1
                
            else:
                tin+=1
        if sin==len(s):
            return True
        return False