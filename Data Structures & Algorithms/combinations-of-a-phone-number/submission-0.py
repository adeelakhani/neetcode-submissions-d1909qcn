class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lookup = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
        }
        if len(digits) == 0:
            return []
        res  = []
        path = []
        def dfs(i, path):
            if i == len(digits):
                res.append("".join(path.copy()))
                return
            

            for j in range(len(lookup[digits[i]])):
                path.append(lookup[digits[i]][j])
                dfs(i+1, path)
                path.pop()
        
        dfs(0, path)
        return res