class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        ans1={}
        ans2={}
        if len(word1)!=len(word2):
            return False
        for i in word1:
            if i not in ans1:
                ans1[i]=0
            else:
                ans1[i]+=1
        for i in word2:
            if i not in ans1:
                return False
            if i not in ans2:
                ans2[i]=0
            else:
                ans2[i]+=1
        arr1=list(ans1.values())
        arr2=list(ans2.values())
        for i in arr1:
            if i in arr2:
                arr2.remove(i)
            else:
                return False
        return True