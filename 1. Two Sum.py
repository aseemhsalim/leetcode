# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ii = 0                  # Store first list item index as 0
        for i in nums[:-1]:     # 1Loop through list except last one.
            jj = 1                  # Store second list item index as 1
            for j in nums[ii+1:]:      # 2Loop through same list except first one
                if i+j == target:       # If target matches sum of current list item of Loop1 and 2
                    return [ii,ii+jj]          # Then return index
                jj = jj + 1             # Increment Loop 2 index
            ii = ii + 1             # Increment Loop 1 index
