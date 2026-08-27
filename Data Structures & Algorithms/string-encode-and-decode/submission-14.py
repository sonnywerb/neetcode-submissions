class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = 1
        while j in range(len(s)):
            if s[j] == "#":
                length = int(s[i:j])
                res.append(s[j + 1: j + 1 + length])
                i = j + 1 + length
                j = i + 1
            else:
                j += 1

        return res
