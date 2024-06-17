from typing import List
from os import system

print(system("clear"))

"""
Given an array of integers,
return indices of the two numbers
such that they add up to a specific target.
"""


def two_sum(nums: List[int], target: int) -> List[int]:
    num_to_index = {}
    for i in range(len(nums)):
        if target - nums[i] in num_to_index:
            return [num_to_index[target - nums[i]], i]
        num_to_index[nums[i]] = i
    return []


print(two_sum([1, 2, 3, 4, 5], 7))
