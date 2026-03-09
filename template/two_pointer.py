def two_pointer(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] + nums[right] == target:
            return [left, right]
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1
    return None

