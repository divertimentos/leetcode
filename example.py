def contains_duplicate(nums):
    hash_table = {}
    for num in nums:
        if num in hash_table:
            return True
        hash_table[num] = 1
    return False


test1 = [1, 2, 3, 1]
test2 = [1, 2, 3, 4]
contains_duplicate([test1])
contains_duplicate([test2])
