class Solution(object):
    def maxDistance(self, colors):
        i,j=0,len(colors)-1
        while colors[0]==colors[j]: j-=1
        while colors[i]==colors[-1]: i+=1
        return max(len(colors)-1-i, j)