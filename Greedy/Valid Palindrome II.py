class Solution:
    def validPalindrome(self, s: str) -> bool:
        i,j=0,len(s)-1
        while i<j:
            if s[i]!=s[j]:
                left,right=s[i+1:j+1], s[i:j]
                return left==left[::-1] or right==right[::-1]
            else:i+=1
            j-=1
        return True

