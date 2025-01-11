#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # TODO: Intitialize  a dictionary to store the index and value 
        arr = {}

        # TODO: Loop through nums and determine its length
        for i in range(len(nums)):
            # Calculate difference between the target and the elements in num
            diff = target - nums[i]

            # Determine if the difference matches with value in dictionary
            if diff in arr:
                # Return the element and its position
                return [arr[diff], i]
            else:
                # Return the element
                arr[nums[i]] = i 
        
# @lc code=end

