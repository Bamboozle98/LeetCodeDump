class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        maxi = 0
        for h in range(0, n + 1):
            count = 0
            for j in range(0, n):
                if citations[j] >= h:
                    count += 1
            if count >= h:
                maxi = max(maxi, h)
        return maxi
