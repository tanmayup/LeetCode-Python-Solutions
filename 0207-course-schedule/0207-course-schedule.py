class Queue:
    def __init__(self):
        self.q = []
        self.front = -1

    def push(self, x):
        if self.front == -1:
            self.front = 0
        self.q.append(x) # Just like stacks

    def pop(self):
        if len(self.q) == 0:
            return -1

        x = self.q[self.front]
        self.front += 1 # we didn't remove the front/first element, we just moved the first pointer ahead
        if self.front == len(self.q): # all elements have been popped
            self.front = -1 # back to -1
            self.q = []
        return x

    def getFront(self):
        if len(self.q) == 0:
            return -1

        return self.q[self.front]

    def size(self):
        if self.front == -1:
            return 0
        
        return len(self.q) - self.front

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        q = Queue()
        ans = []
        indegree = [0] * numCourses

        adjList = []
        for i in range(numCourses):
            adjList.append([])

        for a, b in prerequisites:
            indegree[a] += 1
            adjList[b].append(a)

        for i in range(numCourses):
            if indegree[i] == 0:
                ans.append(i)
                q.push(i)

        while q.size() > 0:
            front = q.pop()
            for x in adjList[front]:
                indegree[x] -= 1
                if indegree[x] == 0:
                    ans.append(x)
                    q.push(x)

        return len(ans) == numCourses