class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        needfreq = {}
        wantedfreq= {}
        left = 0


        for char in s1:

            needfreq[char] = needfreq.get(char, 0) + 1

        for right in range(len(s2)):

            if s2[right] in wantedfreq:

                wantedfreq[s2[right]] += 1

            else:

                wantedfreq[s2[right]] = 1

            

            while (right - left + 1) > len(s1):

                wantedfreq[s2[left]] -=  1

                if wantedfreq[s2[left]] == 0:
                    del wantedfreq[s2[left]]
                left += 1

            if len(s1) == (right - left + 1):

                if needfreq == wantedfreq:

                    return True

        return False
        
        