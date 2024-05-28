class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash={}
        res=0
        for i in s:
            hash[i]=hash.get(i,0)+1
        
        for i in hash.values():
            res+=i//2 * 2
        if any(i%2!=0 for i in hash.values()):
            res+=1
        return res

print(Solution.longestPalindrome(Solution, "abccccdd"))