class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        index = {}

        for i, ele in enumerate(nums):

            index[ele] = i

        for i in range(len(nums)):

            y = target - nums[i]

            if y in index and index[y] != i:

                return [i, index[y]]        