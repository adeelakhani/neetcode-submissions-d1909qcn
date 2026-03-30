from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams: str = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] = count[ord(char) - ord('a')] + 1
            key = tuple(count)
            anagrams[key].append(s)
            return list(anagrams.values()) 

        # default dict makes it so that we can do dict[key].append, instead of
        # having to do dict[key] = [], then dict[key].append
        # key in dict cannot be mutable, so a list as the key wont work, must use tuple
        # so we get a tuple which contains a sort of hashmap but instead is a 26 long array
        # where the 0th element is 'a' and the 25th element represents 'z'
        # then we wanna use that array as the key, and we go through each str, get the array
        # then we append on that key array, so it'll either get added as new, or appeneded to 
        # the other anagrams list. EASY





 