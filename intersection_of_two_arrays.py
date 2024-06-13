from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        inter = []

        for num in nums1:
            if num in nums2 and num not in inter:
                inter.append(num)
        return inter


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
solution = Solution()

print(solution.intersection(nums1, nums2))
