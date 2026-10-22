class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        for i in range(len(words)-1):
            for j in range(min(len(words[i]), len(words[i+1]))):
                if words[i][j] != words[i+1][j]:
                    adj[words[i][j]].add(words[i+1][j])
                    break

        print(adj)
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbour in adj[node]:
                dfs(neighbour)
            res.append(node)

        visited = set()
        res = []
        for letter in list(adj.keys()):
            dfs(letter)

        res.reverse()
        res = "".join(res)
        return res