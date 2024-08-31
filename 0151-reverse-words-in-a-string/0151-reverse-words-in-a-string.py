class Solution:
    def reverseWords(self, s: str) -> str:
        word_split=[]
        word_split=s.split(" ")
        reverse=list(reversed(word_split))
        temp_reverse=[]
        for i in reverse:
            if i:
                temp_reverse.append(i)
        rev_str=" ".join(temp_reverse)
        return rev_str