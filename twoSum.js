/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

var twoSum = function(nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] !== nums[j] && nums[i] + nums[j] === target) {
        return [i, j]
      }
      else if (nums[i] === nums[j] && nums[i] + nums[j] === target) {
        console.log('else if')
        return [i, j]
      }
    }
  }
}

