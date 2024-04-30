class Solution(object):
    def makeSmallestPalindrome(self, s):
        return ''.join(map(min, zip(s, s[::-1])))

        # seven
        # neves
        # (s,n) (e,e) (v,v) (e,e) (n,s)

print(Solution.makeSmallestPalindrome(Solution,'seven'))

