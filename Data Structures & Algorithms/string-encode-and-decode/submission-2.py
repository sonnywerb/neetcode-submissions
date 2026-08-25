class Solution:

    def encode(self, strs: List[str]) -> str:
        # iterate through strs
        # get the length of the string
        # append length + separator (e.g. $ or #) + word
        res = []

        for s in strs:
            encoded_s = []
            encoded_s.append(f"{len(s)}#{s}")
            res.append("".join(encoded_s))
        print("".join(res))
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []

        # 5#Hello5#World
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) # 5
            res.append(s[j + 1: j + 1 + length]) # j = 1, end of word = 6
            i = j + 1 + length

        return res
    
