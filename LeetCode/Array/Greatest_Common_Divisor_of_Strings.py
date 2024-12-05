class Solution(object):
    def gcdOfStrings(self, str1, str2):
        len1 = len(str1)
        len2 = len(str2)

        def isDivisor(i):
            # Check if both string lengths are divisible by i
            if len1 % i != 0 or len2 % i != 0:
                return False
            
            # Calculate the number of repetitions for the substring
            f1, f2 = len1 // i, len2 // i
            
            # Verify if the substring of length i can construct both strings
            return f1 * str1[:i] == str1 and f2 * str1[:i] == str2

        # Iterate from the length of the shorter string down to 1
        for i in range(min(len1, len2), 0, -1):
            if isDivisor(i):
                return str1[:i]  # Return the largest common divisor string

        return ""

# Initialization: The lengths of str1 and str2 are stored in len1 and len2.

# Divisor Check Function: The isDivisor(i) function checks if a substring of length i
#  can evenly divide both strings. 
# It first verifies that both lengths are divisible by i. 
# Then, it checks if repeating the substring str1[:i] 
# the appropriate number of times reconstructs both strings.

# Finding the GCD of Strings: The main loop iterates
# from the length of the shorter string down to 1
# For each length i, it calls isDivisor(i). 
# If a divisor is found, it returns the corresponding substring from str1.

# Return Statement:
#  If no common divisor string is found, it returns an empty string.