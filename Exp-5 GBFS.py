from queue import PriorityQueue

graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['G'],
    'F':['G'],
    'G':[]
}

h = {'A':7,'B':6,'C':4,'D':5,'E':2,'F':1,'G':0}

def greedy(start, goal):
    pq = PriorityQueue()
    pq.put((h[start], start))
    visited = []

    while not pq.empty():
        _, node = pq.get()
        if node not in visited:
            visited.append(node)
            if node == goal:
                return visited
            for i in graph[node]:
                pq.put((h[i], i))

print("Path:", greedy('A','G'))
