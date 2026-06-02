class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range (len(nums)):
            if nums[i] == target:
                return i
            if (i > 0 and (nums[i - 1] < target < nums[i])) or (i == 0 and (target < nums[i])):
                return i
        return i + 1
