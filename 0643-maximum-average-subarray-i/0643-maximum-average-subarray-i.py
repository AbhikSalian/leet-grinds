class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        maxsum=sum(nums[:k])
        temp_sum=maxsum
        for i in range(1,n-k+1):
            temp_sum=temp_sum-nums[i-1]+nums[i+k-1]
            maxsum=max(maxsum,temp_sum)
        return maxsum/k