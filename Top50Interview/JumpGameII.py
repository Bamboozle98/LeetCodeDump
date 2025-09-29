class Solution(object):
    def jump(self, nums):
        n = len(nums)
        if n <= 1:
            return 0
        count = 0
        x = 0
        farthest = 0
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == x:
                count += 1
                x = farthest
                if x >= n - 1:
                    return count
        return count
