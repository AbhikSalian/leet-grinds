class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow=0
        n=len(s)
        for i in range(k):
            if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
                vow+=1
        maxvow=vow
        for i in range(1,n-k+1):
            if s[i-1]=='a' or s[i-1]=='e' or s[i-1]=='i' or s[i-1]=='o' or s[i-1]=='u':
                vow-=1
            if s[i+k-1]=='a' or s[i+k-1]=='e' or s[i+k-1]=='i' or s[i+k-1]=='o' or s[i+k-1]=='u':
                vow+=1
            maxvow=max(maxvow,vow)
        return maxvow