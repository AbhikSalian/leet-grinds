class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        maxop=0
        count={}
        for num in nums:
            complement=k-num
            if complement in count and count[complement]>0:
                maxop+=1
                count[complement]-=1
            else:
                if num in count:
                    count[num]+=1
                else:
                    count[num]=1
        return maxop