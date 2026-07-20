graph = {
    'A': [('B', 4), ('C', 3)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 6)],
    'D': [],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

heuristic = {'A':7,'B':6,'C':4,'D':5,'E':2,'F':1,'G':0}

def best_first(start, goal):
    open = [start]
    visited = []
    while open:
        open.sort(key=lambda x: heuristic[x])
        node = open.pop(0)
        visited.append(node)
        if node == goal:
            return visited
        for n, _ in graph[node]:
            if n not in visited:
                open.append(n)

print("Path:", best_first('A','G'))
