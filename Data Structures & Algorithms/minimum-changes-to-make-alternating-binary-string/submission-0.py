class Solution:
    def minOperations(self, s: str) -> int:

        pat1 = 0
        pat2 = 0

        for i in range(len(s)):

            genpat = '0' if i % 2 == 0 else '1'

            if s[i] != genpat:

                pat1 += 1

        pat2 = len(s) - pat1

        return min(pat2, pat1)




        