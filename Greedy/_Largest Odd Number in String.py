class Solution(object):
    def largestOddNumber(self, num):
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2!=0:
                return num[:i+1]
        return ''

# "We employ a straightforward approach to find the largest odd number within the given string 'num'. Starting from the last digit, we iterate backward through the string. If we encounter an odd digit,
#  we return the substring from the beginning of 'num' to this odd digit, inclusive.
# This ensures that the returned substring represents the largest odd number in 'num'.
# If no odd digit is found, we return an empty string.

# The time complexity of this algorithm is O(N), where N is the length of the input string 'num',
# as we iterate through each digit once. Additionally,
# the space complexity is O(1),
# since we only use a constant amount of extra space for variables regardless of the input size."