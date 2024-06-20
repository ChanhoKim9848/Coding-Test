class Solution(object):
    def containsDuplicate(self, nums):
        n_set = set()
        for n in nums:
            if n in n_set:
                return True
            n_set.add(n)
        
        return False
                
