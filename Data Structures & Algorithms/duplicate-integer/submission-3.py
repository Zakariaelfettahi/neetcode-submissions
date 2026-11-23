class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_array = list(dict.fromkeys(nums))

        if len(nums) == len(new_array):
            return False
        else:
            return True
        