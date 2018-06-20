class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print('input:', nums)
        input_len = len(nums)
        lower_bound = 0
        upper_bound = input_len - 1
        idx = (upper_bound + lower_bound) // 2
        while idx < input_len - 1:
            if nums[idx] == nums[idx + 1]:
                diff = idx - 2 - lower_bound
                if diff % 2 != 0:
                    upper_bound = idx - 1
                else:
                    lower_bound = idx + 2
            else:
                if nums[idx] != nums[idx - 1] and nums[idx] != nums[idx + 1]:
                    return nums[idx]
                else:
                    if nums[idx] == nums[idx - 1]:
                        if (idx - 1 - lower_bound) % 2 != 0:
                            upper_bound = idx - 2
                        else:
                            lower_bound = idx + 1

            if lower_bound >= upper_bound:
                return nums[upper_bound]

            idx = (upper_bound + lower_bound) // 2

        return nums[idx]

print('result:', Solution().singleNonDuplicate([1,1,2]))
print('==='*12)
print('result:', Solution().singleNonDuplicate([1,2,2]))
print('==='*12)
print('result:', Solution().singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
print('==='*12)
print('result:', Solution().singleNonDuplicate([3,3,7,7,10,11,11]))
print('==='*12)
print('result:', Solution().singleNonDuplicate([1,1,2,2,4,4,5,5,9]))
print('==='*12)
