class Solution(object):
    def minTimeToType(self, word):
        p='a'
        res=len(word)
        for i in word:
            val=abs(ord(p)-ord(i))
            res+=min(val,26-val)
            p=i
        return res
        