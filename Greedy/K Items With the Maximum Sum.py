class Solution(object):
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):

        if numOnes >= k:
            return k
        elif numOnes + numZeros >=k:
            return numOnes
        else:
            return numOnes - (k - (numOnes+numZeros))
print(Solution.kItemsWithMaximumSum(Solution,3,3,3,8))

# The objective is to find the maximum sum of k elements using ones, zeros, and negative ones.
# If the count of ones is equal to or exceeds k, we simply take k ones.
# If the sum of counts of ones and zeros is sufficient to meet k, we take all available ones.
# If k exceeds the total of ones and zeros, the surplus is covered by negative ones.

        
