/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  let hashTable = {};
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] in hashTable) {
      return true;
    }

    hashTable[nums[i]] = 1;
  }

  return false;
};

let test1 = [1, 2, 3, 1]; // should return true because there is duplicate (1, 1)
let test2 = [1, 2, 3, 4]; // should return false because there is no duplicates

console.log(containsDuplicate(test1));
console.log(containsDuplicate(test2));
