class Solution:
    def findMin(self, nums: List[int]) -> int:

        low = 0
        high = len(nums) - 1

        while low < high:

            mid = (low + high) // 2

            if nums[low] < nums[high]:

                    return nums[low]

            if nums[low] <= nums[mid]:

                low = mid + 1

            else:

                high = mid

        return nums[low]

                