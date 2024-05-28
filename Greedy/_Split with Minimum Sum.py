class Solution(object):
    def splitNum(self, num):

        # The join() method in Python is used to concatenate elements of an iterable,
        # such as a list, into a single string.
        # It takes the iterable as an argument 
        # and returns a string where each element of the iterable
        # is joined together with the specified separator.
        s = ''.join(sorted(str(num)))
        # # Convert num into a string, sort its characters, and concatenate them, storing the result in s.

        return int(s[::2]) + int(s[1::2])
        # The slicing notation [::2] means taking every second element of the string starting from index 0,
        # and [1::2] means taking every second element starting from index 1.
        # Split the string into two parts and calculate the sum of corresponding digits.
        # For instance, if the string is "123456", then the sum would be 135 + 246.
        