class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                # print(nums[i], nums[i+1])
                if nums[i] + nums[j] == target:
                    return [i, j]

