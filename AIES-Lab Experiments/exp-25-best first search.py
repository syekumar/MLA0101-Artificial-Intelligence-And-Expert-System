graph = {
    'A':[('B',6),('C',2)],
    'B':[('D',5)],
    'C':[('D',1)],
    'D':[('E',0)],
    'E':[]
}

visited=[]

def best_first(start,goal):

    queue=[(0,start)]

    while queue:

        queue.sort()

        h,node=queue.pop(0)

        if node not in visited:

            print(node,end=" ")

            visited.append(node)

            if node==goal:
                print("\nGoal Reached")
                return

            for neighbor,cost in graph[node]:
                queue.append((cost,neighbor))

best_first('A','E')
