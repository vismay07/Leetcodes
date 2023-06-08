# 283. Move Zeroes
# Easy
# 13.8K
# 348
# Companies
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.


# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]


# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr = -1

        for i in range(len(nums) - 1):
            k = i + 1
            curr = nums[i]
            if nums[i] == 0:
                while k < len(nums) - 1 and nums[k] == 0:
                    k += 1
                nums[i] = nums[k]
                nums[k] = curr

