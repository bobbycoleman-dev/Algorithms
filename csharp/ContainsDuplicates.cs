using System.Collections.Generic;
using System.Linq;

public class Solution
{
    int[] nums1 = [1, 2, 3, 1];
    int[] nums2 = [1, 2, 3, 4];
    int[] nums3 = [1, 1, 1, 2, 2, 2, 3, 4];

    public bool ContainsDuplicates(int[] nums)
    {
        List<int> seen = new();

        for (int i = 0; i < nums.Length; i++)
        {
            if (seen.Contains(nums[i]))
            {
                return true;
            }
            else
            {
                seen.Add(nums[i]);
            }
        }

        return false;

    }
}