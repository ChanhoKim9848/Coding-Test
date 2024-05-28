class Solution(object):
    def minOperations(self, nums):
        # Initialize a variable to keep track of the total number of operations
        total_operations = 0
        
        # Iterate through the array, considering each pair of adjacent elements
        for i in range(len(nums) - 1):
            # Check if the current element is greater than or equal to the next element
            if nums[i] >= nums[i + 1]:
                # Calculate the difference between the current element and the next element,
                # and add 1 to it to ensure that the next element becomes strictly greater
                difference = nums[i] - nums[i + 1] + 1
                nums[i + 1] += difference
                
                # Increment the total number of operations by the calculated difference
                total_operations += difference
        
        # Return the total number of operations required to make the array strictly increasing
        return total_operations


print(Solution.minOperations(Solution,[1,2,2]))

# we loop through nums array and check if an element on current index is less than next element in the array
# if not, then we add up the difference between them and plus 1 to the next element, so that we make the array
# is strictly increasing and also save to res to keep tracking how much we actually add up 
# after the loop, we return res

# the algorithm loop through the array once, so time complexity is O(N), where N is the size of the array
# It uses constant space and doesn't utilize any data structures that grow with the input size.
# Hence, the space complexity is O(1)