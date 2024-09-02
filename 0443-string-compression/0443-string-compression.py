class Solution:
    def compress(self, chars: List[str]) -> int:
        temp='' 
        count=1
        n=len(chars)
        tempchars=chars.copy()
        chars.clear()
        for i in range(n):
            if tempchars[i]==temp:
                count+=1
                lenchar=n-1
                if i==lenchar:
                    chars.extend(list(str(count)))
            else:
                if count==1:
                    chars.append(tempchars[i])
                    temp=tempchars[i]
                else:
                    chars.extend(list(str(count)))
                    chars.append(tempchars[i])
                    count=1
                    temp=tempchars[i]
        return len(chars)