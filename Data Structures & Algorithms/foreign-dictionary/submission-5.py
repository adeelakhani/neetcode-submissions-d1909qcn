class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        
        for i in range(len(words)):
            for j in range(len(words[i])):
                adj[words[i][j]]
        for i in range(len(words)-1):
            foundSum = False
            for j in range(min(len(words[i]), len(words[i+1]))):
                if words[i][j] != words[i+1][j]:
                    adj[words[i][j]].add(words[i+1][j])
                    foundSum = True
                    break
            if foundSum == False and len(words[i]) > len(words[i+1]):
                return ""

        print(adj)
        def dfs(node, path):
            if node in path:
                return False
            if node in visited:
                return
            path.add(node)
            visited.add(node)
            for neighbour in adj[node]:
                if dfs(neighbour, path) == False:
                    return False
            path.discard(node)
            res.append(node)

            return True

        visited = set()
        path = set()
        res = []
        for letter in list(adj.keys()):
            if dfs(letter, path) == False:
                return ""

        res.reverse()
        res = "".join(res)
        return res