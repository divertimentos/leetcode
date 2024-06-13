from functools import reduce
import os
os.system("clear")


class Solution:

    def isHappy(self, n: int) -> bool:

        array_of_n = ([int(digit) for digit in str(n)])
        # print(f"array of n: {array_of_n}")

        squared_array = list(map(lambda num: num ** 2, array_of_n))
        # print(f"squared array: {squared_array}")

        def sum(n1, n2):
            return n1 + n2

        array_sum = reduce(lambda num1, num2: num1 + num2, squared_array)

        if array_sum == 1:
            return True

        return self.isHappy(array_sum)


test = Solution()

print(test.isHappy(19))
# print(test.isHappy(82))
# print(test.isHappy(68))
# print(test.isHappy(100))
