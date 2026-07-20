import heapq

def ucs(graph, start, goal):
    priority_queue = [(0, start, [start])]
    visited = set()

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        if node == goal:
            return cost, path

        if node not in visited:
            visited.add(node)

            for neighbour, weight in graph[node]:
                if neighbour not in visited:
                    heapq.heappush(priority_queue,
                                   (cost + weight,
                                    neighbour,
                                    path + [neighbour]))

    return None

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 1)],
    'E': [('G', 2)],
    'F': [('G', 2)],
    'G': []
}

result = ucs(graph, 'A', 'G')
print("Cost:", result[0])
print("Path:", result[1])
