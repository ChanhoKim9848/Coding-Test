class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # return Counter(s) == Counter(t)

        if len(s)!=len(t):
            return False
        
        countS, countT = {},{}
        for i in range(len(s)):
            countS[s[i]]=1+countS.get(s[i],0)
            countT[t[i]]=1+countT.get(t[i],0)
        
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True
    # we iterate two strings and count each character
    # and we compare if one string has exactly same characters as the other one. return True
    # we can use hashmap to count the number of each character of the string
    # and we compare by iterating hashmap if it is not the same number then it return false
    # time complexity O(S+T), we iterate through two strings, 
    # space complexity O(S+T), as we make two hashmaps
    
