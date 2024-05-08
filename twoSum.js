/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  let result
  let iValue
  let jValue

  for (let i = 0; i < nums.length; i++) {
    for (let j = 0; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        console.log('iValue', nums[i])
        console.log('jValue', nums[j])
        return [i, j]
      }


    }
  }
  return []
}
