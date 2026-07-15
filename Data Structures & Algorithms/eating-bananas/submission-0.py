class Solution:

    def canFinish(self, k, piles):

        totalhours = 0

        for pile in piles:

            totalhours += (pile + k - 1) // k

        return totalhours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low = 1
        high = max(piles)

        while low <= high:

            mid = (low + high) // 2

            if self.canFinish(mid, piles) <= h:

                high = mid - 1

            else:

                low = mid + 1

        return low




        