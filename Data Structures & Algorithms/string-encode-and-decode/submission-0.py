class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += len(s) + s
        return string
    def decode(self, s: str) -> List[str]:
        strs = []
        # i = s[0]
        for i in range(0, s):
            length = int(s[i])
            newWord = ""
            for j in range(1, length+1):
                newWord += s[j]
            strs.append(newWord)
            i+=length
        return strs
