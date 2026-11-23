class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # remove duplicates and sort
        clean_nums = sorted(list(set(nums)))
        size = len(clean_nums) -1 

        max_len =1
        i=0
        while i < size:
            j = i
            while j< size and clean_nums[j+1] - clean_nums[i] ==1+j-i:
                j += 1 
            
            max_len = max(max_len, j - i + 1)
            i =j+1
        return max_len