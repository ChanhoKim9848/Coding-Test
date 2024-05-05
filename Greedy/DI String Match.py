import collections
class Solution(object):
    def diStringMatch_deque(self, s):

        a=collections.deque(range(len(s) + 1))
        res=[]

        for i in s : 
            if i == 'I':
                res.append(a.popleft())
            else:res.append(a.pop())
        res.append(a.pop())
        return res

print(Solution.diStringMatch(Solution,"IDID"))

# two pointer
# go inward and each time get the minimum and maximum
# time: O(N)
# space: O(N)










