from itertools import accumulate
from bisect import bisect_right
class Solution(object):

    def answerQueries(self, nums,queries):
        nums = list(accumulate(sorted(nums)))
        return [bisect_right(nums, q) for q in queries]
        
print(Solution.answerQueries(Solution,[1,3,5,7,9],[3,4,5]))
