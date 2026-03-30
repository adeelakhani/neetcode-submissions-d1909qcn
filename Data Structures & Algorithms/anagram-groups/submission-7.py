class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # get the char, then get the value relative to alphabet, so a = 0, z=25
        # convert this to tuple, and use as key for hashmap
        hashmap = {}
        for s in strs:
            alphabet = [0] * 26
            for st in s:
                pos = ord(alphabet) - 97
                alphabet[pos] += 1
            hashmap[tuple(alphabet)].append(s)



