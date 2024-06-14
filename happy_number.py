from functools import reduce
import os

os.system("clear")


class Solution:

    def isHappy(self, n: int, visited=None) -> bool:
        if visited is None:
            visited = set()

        if n == 1:
            return True

        if n in visited:
            return False

        visited.add(n)

        digits_of_n = ([int(digit) for digit in str(n)])
        squared_digits = list(map(lambda num: num ** 2, digits_of_n))
        reduced = reduce(lambda num1, num2: num1 + num2, squared_digits)

        return self.isHappy(reduced, visited)


test_case = Solution()

# print(test_case.isHappy(19))
# print(test_case.isHappy(82))
# print(test_case.isHappy(68))
# print(test_case.isHappy(100))

# print(test_case.isHappy(1))
# print(test_case.isHappy(2))
# print(test_case.isHappy(20))
