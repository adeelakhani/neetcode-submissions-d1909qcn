class Solution:

    def encode(self, strs: List[str]) -> str:
        lengths = []
        encoded = ""
        for s in strs:
            lengths.append(len(s))
        for i in range(0, len(strs)):
            encoded+= str(lengths[i])
            encoded += strs[i]
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []
        index = 0
        for i in range(0, len(s)):
            print(s)
            print(index)
            length = int(s[index])
            print(length)
            index += 1
            temp = ""
            for i in range(index, index + length):
                temp += s[i]
                index+=1
            decoded.append(temp)
            if index == len(s):
                break
        return decoded
