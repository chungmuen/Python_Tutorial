def two_sum(nums, target):
    if isinstance(target, str):
        raise TypeError("The target should be a number.")
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]
