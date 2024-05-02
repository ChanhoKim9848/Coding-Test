class Solution(object):
    def getLongestSubsequence(self, words, groups):
        prev=-1
        res=[]
        for i in range(len(groups)):
            if prev!=groups[i]:
                res.append(words[i])
                prev=groups[i]
        return res