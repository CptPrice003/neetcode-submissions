class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numset = set(nums)
        maxlen = 0
        length = 0


        for num in numset:

            if num - 1 not in  numset:

                cur = num
                length = 1

                while cur + 1 in numset:

                    length += 1
                    cur += 1
                maxlen = max(maxlen, length)

        return maxlen

                    
        