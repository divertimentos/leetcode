import os


def contains_duplicate(numsArray):
    hash_table = {}
    for i in numsArray:
        if i in hash_table:
            return True

        hash_table[i] = 1

        print(hash_table)
    return False


test1 = [1, 2, 3, 1]  # should return true because there is duplicate (1, 1)
test2 = [1, 2, 3, 4]  # should return false because there is no duplicates

os.system("clear")
print(contains_duplicate(test1))  # true
print(contains_duplicate(test2))  # false
