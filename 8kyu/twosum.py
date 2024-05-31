def twoSum(nums: list[int], target: int) -> list[int]:
    for x in nums:
        if (target - x) in nums[nums.index(target - x) + 1:]:
            outs = [nums.index(x), nums.index(target - x)]
            return outs
    return None


nums = [3, 3]
target = 6

print(twoSum(nums, target))
