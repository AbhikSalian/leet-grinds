class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left=0
        right=0
        tk=1
        maxlen=0
        for i in range(len(nums)):
            if nums[i]==0:
                if tk<=0:
                    if nums[left]==0:
                        right+=1
                        left+=1
                    else:
                        while nums[left]!=0:
                            left+=1
                        left+=1
                        right+=1
                else: 
                    tk-=1
                    right+=1
            else:
                right+=1
            # temp_arr=nums[left:right]
            maxlen=max(maxlen,right-left)
        return maxlen-1