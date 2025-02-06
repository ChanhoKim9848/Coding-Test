class Solution:
    def groupAnagrams(self, strs):
        h=defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            h[sorted_s].append(s)
        return list(h.values())