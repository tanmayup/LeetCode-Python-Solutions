class Solution:
    def dijkstra(self, graph, source):
        import heapq
        n = len(graph)

        dist = [float("inf")] * (n + 1)
        dist[source] = 0

        visited = [False] * (n + 1) 
        heap = [(0, source)]

        while heap:
            curr_dist, node = heapq.heappop(heap)

            if visited[node]:
                continue

            visited[node] = True

            for neighbour, weight in graph[node]:
                if curr_dist + weight < dist[neighbour]:
                    dist[neighbour] = curr_dist + weight
                    heapq.heappush(heap, (dist[neighbour], neighbour))
        dist.remove(float("inf"))        

        return dist

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        nodes = [i for i in range(1, n+1)]
        el = []
        for _ in range(n):
            el.append([])

        adjList = dict(zip(nodes, el))

        for el in times:
            adjList[el[0]].append(el[1:])

        return max(self.dijkstra(adjList, k)) if max(self.dijkstra(adjList, k)) != float("inf") else -1