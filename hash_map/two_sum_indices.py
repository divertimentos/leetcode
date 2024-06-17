from os import system
from typing import List

system("clear")


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i in nums:
            if (target - nums[i]) in num_to_index:
                return []
            # num_to_index[nums[nums[i]]] = nums[i]

        return []


nums1 = [2, 7, 11, 15]

test_case = Solution()
print(test_case.twoSum(nums1, 9))
