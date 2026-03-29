class Solution:

    def encode(self, strs: List[str]) -> str:
        lengths = []
        encoded = ""
        for s in strs:
            tag = "" + str(len(s)) + "@"
            lengths.append(tag)
        for i in range(0, len(strs)):
            encoded+= lengths[i]
            encoded += strs[i]
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []
        index = 0
        for i in range(0, len(s)):
            length = ""
            for j in range(index, len(s)):
                length += s[j]
                index += 1
                if s[index] == "@":
                    index+=1
                    break
            length = int(length)

            temp = ""
            for i in range(index, index + length):
                temp += s[i]
                index+=1
            decoded.append(temp)
            if index == len(s):
                break
        return decoded
