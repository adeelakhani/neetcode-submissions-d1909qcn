class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + "$" + s
        print(string)
        return string

    def decode(self, s: str) -> List[str]:
        strs = []
        # i = s[0]
        i = 0
        while i < len(s):
            # if s[i].isdigit():
            # length = int(s[i])
            length = ""
            for j in range(i, len(s)):
                char = s[j]
                # print("char " + char)
                if char == "$":
                    break
                length += char
            toSkip = len(length) + 1
            length = int(length)
            print("length", length)
            # print("toSkip", toSkip)
            print("Going from ", i + toSkip, "to ", i + toSkip + length + 1)
            newWord = ""
            for j in range(i + toSkip, i + toSkip + length + 1):
                newWord += s[j]
            strs.append(newWord)
            print("newWord", newWord)
            i += length + 1
            i+=1
        return strs
