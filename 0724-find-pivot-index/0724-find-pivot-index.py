class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if sum(nums[0:i])==sum(nums[i+1:n]):
                return i
        return -1