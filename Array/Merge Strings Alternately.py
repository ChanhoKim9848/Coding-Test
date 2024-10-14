class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j=0,0
        res=[]
        while i<len(word1) and j<len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i+=1
            j+=1
        res.append(word1[i:])
        res.append(word2[j:])

        return "".join(res)

# time complexity O(N+M), where N is the length of word1, M is the length of word2
# we check every single word in word1 and word 2
# 14/10/24