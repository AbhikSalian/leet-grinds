class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=[]
        n=len(s)
        for i in range(n):
            if s[i]=='a' or s[i]=='A' or s[i]=='e' or s[i]=='E' or s[i]=='i' or s[i]=='I' or s[i]=='o' or s[i]=='O' or s[i]=='u' or s[i]=='U':
                vowels.append(s[i])
        vowels.reverse()
        j=0
        for i in range(n):
            if s[i]=='a' or s[i]=='A' or s[i]=='e' or s[i]=='E' or s[i]=='i' or s[i]=='I' or s[i]=='o' or s[i]=='O' or s[i]=='u' or s[i]=='U':
                s=s[:i]+vowels[j]+s[i+1:]
                j+=1
        return s