class Solution(object):
    def productExceptSelf(self, nums):
        a=1
        z=0
        result=[]
        for i in nums:
            if i==0:
                z+=1
            else: a*=i
        for i in nums:
            if i==0:
                if z-1>0:
                    result.append(0)
                else: result.append(a)
            elif z>0:result.append(0)
            else:result.append(a/i)
        return result
