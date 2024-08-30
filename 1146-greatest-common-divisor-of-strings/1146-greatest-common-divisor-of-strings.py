class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1=len(str1)
        len2=len(str2)
        flag1=False
        flag2=False
        gcd=""
        if len1<len2:
            min_str=str1
            max_str=str2
        else:
            min_str=str2
            max_str=str1
        for i in range((len(min_str)),0,-1):
            temp=min_str[:i]
            if len(min_str)%len(temp)==0 and len(max_str)%len(temp)==0:
                min_div=len(min_str)//len(temp)
                max_div=len(max_str)//len(temp)
                temp_minstr=""
                temp_maxstr=""
                for j in range(min_div):
                    temp_minstr=temp_minstr+temp
                if temp_minstr==min_str:
                    flag1=True
                for j in range(max_div):
                    temp_maxstr=temp_maxstr+temp
                if temp_maxstr==max_str:
                    flag2=True
                if flag1==True and flag2==True:
                    return temp
            flag1=False
            flag2=False
        return gcd