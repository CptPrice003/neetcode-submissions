class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        seen = set()

        for ele in nums:

            if ele in seen:

                return ele

            else:

                seen.add(ele)
        