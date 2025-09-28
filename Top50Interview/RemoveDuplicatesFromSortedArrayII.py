class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        k = 1
        counter = 1
        length = len(nums)
        current_value = nums[0]
        for i in range (1, length):
            if nums[i] == current_value:
                if counter < 2:
                    nums[k] = nums[i]
                    k += 1
                    counter += 1
                else:
                    continue
            else:
                current_value = nums[i]
                counter = 1
                nums[k] = nums[i]
                k += 1
        return k
            
