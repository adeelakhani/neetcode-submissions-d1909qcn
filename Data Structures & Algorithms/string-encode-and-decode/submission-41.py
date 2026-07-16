class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s))+s)
        return "".join(encoded)
    def decode(self, s: str) -> List[str]:
        res = []
        c = 0
        while c<len(s):
            length = int(s[c])
            c+=1
            currIndex = c
            string = ""
            while c < len(s) and c < currIndex + length:
                string += s[c]
                c+=1
            res.append(string)
        return res
                
