class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        return sorted(s)==sorted(t) 
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)

        for i in s:
            count[i]+=1
        for j in t:
            count[j]-=1
        
        for i in count.values():
            if i != 0:
                return False
        return True
        
        