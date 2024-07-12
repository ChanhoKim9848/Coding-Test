class Solution(object):
    def topKFrequent(self, nums, k):
        # Create a hashmap to count the frequency of each element
        frequency_map = {}
        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1

        # Create a list of empty lists to group numbers by their frequency
        frequency_buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in frequency_map.items():
            frequency_buckets[freq].append(num)

        result = []

        # Iterate over the frequency_buckets from highest to lowest frequency
        for freq in range(len(frequency_buckets) - 1, 0, -1):
            for num in frequency_buckets[freq]:
                result.append(num)
                # Once we have k elements in the result, return it
                if len(result) == k:
                    return result