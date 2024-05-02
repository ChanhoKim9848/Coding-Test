class Solution(object):
    def minimumPushes(self, word):
        res = 0
        # Loop through each letter in the word
        for i in range(len(word)):
            # Calculate the number of times to push based on the current position
            # and the pattern of pushing the keys
            res += i // 8 + 1
        # Return the total number of pushes required
        return res

        
# Time : O(N)
# Space: O(1)


# We aim to determine the minimum number of pushes required to type a given word.
# We achieve this by iteratively mapping the first 8 letters to each dial on the keypad.
# After mapping the initial 8 letters, for every subsequent 8 letters, an additional push is needed.
# Therefore, for each letter in the word, we calculate the number of pushes required based on its position
# relative to the pattern of pushing keys.
# Finally, we return the total number of pushes needed.


