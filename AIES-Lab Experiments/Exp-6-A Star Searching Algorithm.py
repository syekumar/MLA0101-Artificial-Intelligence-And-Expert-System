from queue import PriorityQueue

graph = {
'A':[('B',1),('C',3)],
'B':[('D',3),('E',1)],
'C':[('F',5)],
'D':[],
'E':[('G',2)],
'F':[('G',2)],
'G':[]
}

h = {'A':7,'B':6,'C':4,'D':5,'E':2,'F':1,'G':0}

def astar(start, goal):
    pq = PriorityQueue()
    pq.put((0,start))
    cost = {start:0}
    parent = {start:None}

    while not pq.empty():
        _, node = pq.get()
        if node == goal:
            break
        for nxt,w in graph[node]:
            new = cost[node]+w
            if nxt not in cost or new<cost[nxt]:
                cost[nxt]=new
                pq.put((new+h[nxt],nxt))
                parent[nxt]=node

    path=[]
    while goal:
        path.append(goal)
        goal=parent[goal]
    return path[::-1]

print("Optimal Path:", astar('A','G'))
