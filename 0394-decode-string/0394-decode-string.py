class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        current=""
        cnum=0
        for i in s:
            if i.isdigit():
                cnum=cnum*10+int(i)
            elif i=='[':
                stack.append((current,cnum))
                current=""
                cnum=0
            elif i==']':
                temp_str,num=stack.pop()
                current=temp_str+(current*num)
            else:
                current+=i
        return current