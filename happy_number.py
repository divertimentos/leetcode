from functools import reduce
import os

os.system("clear")


class Solution:

    def isHappy(self, n: int, visited=None) -> bool:
        if n == 1:
            return True

        if visited is None:
            visited = set()

        if n in visited:
            return False

        visited.add(n)

        digits_of_n = ([int(digit) for digit in str(n)])
        squared_digits = list(map(lambda num: num ** 2, digits_of_n))
        reduced = reduce(lambda num1, num2: num1 + num2, squared_digits)

        return self.isHappy(reduced, visited)


test_case = Solution()

print(f"19: {test_case.isHappy(19)}")
# print(test_case.isHappy(82))
# print(test_case.isHappy(68))
# print(test_case.isHappy(100))

print(f"1: {test_case.isHappy(1)}")
print(f"2: {test_case.isHappy(2)}")
print(f"20: {test_case.isHappy(20)}")
