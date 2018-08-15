from collections import deque

wall_allowance = 1

class Node:
    def __init__(self, x,y, destroyed, graph):
        self.x = x
        self.y = y
        self.walls_destroyed = destroyed
        self.graph = graph

    def __hash__(self):
        return self.x ^ self.y

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y) and (self.walls_destroyed == other.walls_destroyed)

    def get_neighbors(self):
        neighbors = []
        x = self.x
        y = self.y
        walls_destroyed = self.walls_destroyed
        graph = self.graph

        ##  Check Left
        if y > 0:
            if graph[x][y-1]:
                if walls_destroyed < wall_allowance:
                    neighbors.append(Node(x,y-1, walls_destroyed+1, graph))
            else:
                neighbors.append(Node(x,y-1, walls_destroyed, graph))
        ##  Check Right
        if y < len(graph[0])-1:
            if graph[x][y+1] == 1:
                if walls_destroyed < wall_allowance:
                    neighbors.append(Node(x,y+1, walls_destroyed+1, graph))
            else:
                neighbors.append(Node(x,y+1, walls_destroyed, graph))
        ##  Check Up
        if x > 0:
            #print "up:      " + str(graph[x - 1][y])
            if (graph[x-1][y] == 1):
                if walls_destroyed < wall_allowance:
                    neighbors.append(Node(x-1,y, walls_destroyed+1, graph))
            else:
                neighbors.append(Node(x-1,y, walls_destroyed, graph))
        ##  Check Down
        if x < len(graph)-1:
            #print "down:    " + str(graph[x + 1][y])
            if (graph[x + 1][y] == 1):
                if walls_destroyed < wall_allowance:
                    neighbors.append(Node(x+1,y, walls_destroyed+1, graph))
            else:
                neighbors.append(Node(x+1,y, walls_destroyed, graph))

        return neighbors

class Graph:
    def __init__(self, maze, start, end):
        self.graph = maze
        self.rows = len(maze)
        self.columns = len(maze[0])
        self.start = start
        self.end = end
        self.nodes = {}

    def dfs_shortest(self):
        start = Node(self.start[0], self.start[1], 0, self.graph)
        queue = deque([start])

        path_distance = {start: 1}

        while queue:
            cur = queue.popleft()
            if (cur.x == self.end[0]) and (cur.y == self.end[1]):
                return path_distance[cur]

            for neighbor in cur.get_neighbors():
                if neighbor not in path_distance.keys():
                    path_distance[neighbor] = path_distance[cur] + 1
                    queue.append(neighbor)
        return -1

def answer(maze):
    graph = Graph(maze, (0,0), (len(maze) - 1, len(maze[0]) - 1))
    return graph.dfs_shortest()
