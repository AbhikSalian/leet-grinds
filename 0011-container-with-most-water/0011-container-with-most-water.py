class Solution:
    def maxArea(self, height: List[int]) -> int:
        def findArea(a,b,ix):
            c=min(a,b)
            ar=c*ix
            if ar>=maxar:
                return ar
            else:
                return maxar
        maxar=0
        n=len(height)
        left=0
        right=n-1
        while left<right:
            maxar=findArea(height[left],height[right],right-left)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxar