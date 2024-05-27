/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
  let hashTable = {}
  // for (let i=0; i < nums.length; i++) {
  //   if (nums[i] in hashTable) {
  //     return true
  //   }
  //   hashTable[]
  // }


  return false
};

let test1 = [1, 2, 3, 1]
let test2 = [1, 2, 3, 4]

// console.log(containsDuplicate(test1))
// console.log(containsDuplicate(test2))

let hashTable = {}
console.log(hashTable[test1[0]] = 1)
console.log(hashTable)

console.log(hashTable[test1[1]] = 1)
console.log(hashTable)

console.log(hashTable[test1[3]] = 1)
console.log(hashTable)
