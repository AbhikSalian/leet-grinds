class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result=[]
        for i in range(len(candies)):
            temp_candy=extraCandies+candies[i]
            if temp_candy>=max(candies):
                result.append(True)
            else:
                result.append(False)
        return result

