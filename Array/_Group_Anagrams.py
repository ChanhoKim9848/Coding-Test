from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        ans = defaultdict(list) #mapping char Count to list of Anagrams

        for s in strs:
            count = [0] * 26  # a ... z
            for c in s:
                count[ord(c) - ord("a")] += 1
                # we count how many of each character we have and save into count
                # we want to group all anagrams with this particular count together

                # strs are like abc, cba
                # abc, cba will have the same count array like
                # a:1, b:1, c:1, so it's going to be count = [1,1,1,0,0,....0]
                # we append and group all anagrams with this particular count together
                # in the list, [1,1,1,0,0,0...0]:[abc,cba]
                
                # list cannot be a key so we change count to tuple
                # as tuple is immutable and unchangable, which means can be a key
                # so each key grouped all anagrams that have 
                # the same count 
            ans[tuple(count)].append(s)
        return ans.values()
# Big O(s * c), space: O(s)

print(Solution.groupAnagrams(Solution,["act","pots","tops","cat","stop","hat"]))