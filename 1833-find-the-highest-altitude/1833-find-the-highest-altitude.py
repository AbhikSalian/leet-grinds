class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n=len(gain)
        pf=[0 for i in range(n+1)]
        for i in range(n):
            pf[i+1]=pf[i]+gain[i]
        maxalt=max(pf)
        return maxalt