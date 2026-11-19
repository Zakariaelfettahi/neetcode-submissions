from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for number in nums:
            if number not in hashmap:
                hashmap[number] = 1
            else:
                hashmap[number] += 1
        return [number for number, frequency in Counter(hashmap).most_common(k)]