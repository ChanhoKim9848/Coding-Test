# Calculate the sum: First, calculate the total sum of the array elements.
# Check if it's divisible: Ensure that the total sum is divisible by 3. If not,
# it's impossible to divide it into three equal parts.
# Find partitions: Iterate through the array, keeping track of the current sum.
# When the current sum reaches one-third of the total sum, it implies the first partition.
# Similarly, when it reaches two-thirds, it implies the second partition.
# The rest belongs to the third partition.
# Check for validity: After finding the potential partitions,
# ensure they are not empty and their sums are equal.
# If so, return True, otherwise False.

class Solution(object):
    def canThreePartsEqualSum(self, arr):
        total_sum = sum(arr)
        if total_sum % 3 != 0:
            return False
        
        avg = total_sum // 3
        partition_sum = 0
        partition_count = 0
        
        for num in arr:
            partition_sum += num
            if partition_sum == avg:
                partition_sum = 0
                partition_count += 1
                
        return partition_count >= 3
