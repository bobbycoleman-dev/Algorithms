# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

nums1 = [2, 7, 11, 15]
target1 = 9
# Output: [0,1]

nums2 = [3, 2, 4]
target2 = 6
# Output: [1,2]

nums3 = [3, 3]
target3 = 6
# Output: [0,1]


def twoSum(nums, target):
    n = len(nums)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# print(twoSum(nums1, target1))
# print(twoSum(nums2, target2))
# print(twoSum(nums3, target3))


def twoSum2(nums, target):
    map = {}
    n = len(nums)

    for i in range(n):
        c = target - nums[i]
        if c in map:
            return [map[c], i]
        map[nums[i]] = i

    return []


print(twoSum2(nums1, target1))
print(twoSum2(nums2, target2))
print(twoSum2(nums3, target3))
