class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ''

        for word in strs:

            res += str(len(word))+'#'+word

        return res


    def decode(self, s: str) -> List[str]:

        
        length = ""
        i = 0
        res = []
        while i < len(s):

            if s[i] != '#':

                length += s[i]
                i += 1

            else:
                i += 1
                length = int(length)
                res.append(s[i: i + length])
                i += length
                length = ""

        return res






