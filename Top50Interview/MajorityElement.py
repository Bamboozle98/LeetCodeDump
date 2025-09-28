class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        current_count = 0
        current_var = nums[0]
        alt_count = 0
        for i in range(0, length):
            if nums[i] == current_var:
                current_count += 1
            if nums[i] != current_var:
                alt_count += 1
            if alt_count > current_count:
                current_var = nums[i]
                current_count = 0
                alt_count = 0
        return current_var
