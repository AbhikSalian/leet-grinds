class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arl=set(arr)
        counts=[]
        for i in arl:
            countr=arr.count(i)
            if countr in counts:
                return False
            else:
                counts.append(countr)
        return True