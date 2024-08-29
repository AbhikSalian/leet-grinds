class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged=""
        len1=len(word1)
        len2=len(word2)
        i=0
        j=0
        while i<len1 or j<len2:
            if i<len1:
                merged+=word1[i]
                i+=1
            if j<len2:
                merged+=word2[j]
                j+=1
        return merged