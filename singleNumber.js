/**
 * @param {number[]} nums
 * @return {number}
 */

var singleNumber = function (nums) {
  let hashTable = {};

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] in hashTable) {
      hashTable[nums[i]] = 2;
    } else {
      hashTable[nums[i]] = 1;
    }
  }

  return Object.keys(hashTable).find((key) => hashTable[key] === 1);
};

const nums1 = [2, 2, 1]; // 1
const nums2 = [4, 1, 2, 1, 2]; // 4
const nums3 = [1]; // 1

console.log(singleNumber(nums1));
console.log(singleNumber(nums2));
console.log(singleNumber(nums3));
