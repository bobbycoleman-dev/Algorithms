nums1 = [1, 2, 3, 1]  # True
nums2 = [1, 2, 3, 4]  # False
nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]  # True


def contains_duplicates(nums):
    freq = {}
    for i in range(len(nums)):
        if nums[i] in freq:
            return True
        else:
            freq[nums[i]] = 1

    return False


print(contains_duplicates(nums1), "should equal True")
print(contains_duplicates(nums2), "should equal False")
print(contains_duplicates(nums3), "should equal True")
