class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n=len(grid)
        gdict={}
        ans=0
        def addToBucket(arr):
            s=sum(arr)
            if s not in gdict:
                gdict[s]=[arr]
            else:
                gdict[s].append(arr)
        for i in range(n):
            addToBucket(grid[i])
        for j in range(n):
            column=[col[j] for col in grid]
            if sum(column) in gdict:
                ans+=gdict[sum(column)].count(column)
        return ans