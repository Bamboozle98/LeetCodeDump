class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        k = 0
        for i in nums:
            if i != val:
                nums[k] = i
                k += 1
            print(nums)
        return k
