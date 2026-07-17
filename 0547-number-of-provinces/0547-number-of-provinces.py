class Solution:
    def dfs(self, node, adjMatrix, visited):
        visited[node] = True
        for x in range(len(adjMatrix)):
            if adjMatrix[node][x] == 1 and not visited[x]:
                self.dfs(x, adjMatrix, visited)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False] * len(isConnected)
        ans = 0
        for i in range(len(isConnected)):
            if not visited[i]:
                self.dfs(i, isConnected, visited)
                ans += 1

        return ans