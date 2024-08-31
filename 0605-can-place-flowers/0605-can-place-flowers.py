class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        possible=0
        for i in range(len(flowerbed)):
            if len(flowerbed)==1:
                if flowerbed[i]==0:
                    possible=1
                else:
                    possible=0
            else:
                if i==0:
                    if (flowerbed[i+1]==0 or (not flowerbed[i+1])) and flowerbed[i]==0:
                        possible+=1
                        flowerbed[i]=1
                if i==len(flowerbed)-1:
                    if (flowerbed[i-1]==0 or (not flowerbed[i-1])) and flowerbed[i]==0:
                        possible+=1
                        flowerbed[i]=1
                else:
                    if flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                        possible+=1
                        flowerbed[i]=1
        if possible >= n:
            return True
        else:
            return False