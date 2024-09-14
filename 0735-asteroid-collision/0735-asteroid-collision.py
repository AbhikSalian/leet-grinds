class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans=[]
        for i in asteroids:
            if i>0:
                ans.append(i)
            elif i<0:
                if len(ans)==0 or ans[-1]<0:
                    ans.append(i)
                while len(ans)>0 and abs(i)>=ans[-1] and ans[-1]>0:
                    if abs(i)==ans[-1]:
                        ans.pop()
                        break
                    else:
                        temp=ans.pop()
                        if (len(ans)==0 or ans[-1]<0) and temp!=abs(i):
                            ans.append(i)
        return ans