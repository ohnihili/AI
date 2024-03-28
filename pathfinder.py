import sys
from collections import deque

mapgrid = sys.argv[1]
alg = sys.argv[2]
heur = sys.argv[3]

# function to read the map file
def read_map(file):
    with open(file, 'r') as file:
        # Read map size
        rows, cols = map(int, file.readline().split())
        
        # Read start and end positions
        start = tuple(map(int, file.readline().split()))
        end = tuple(map(int, file.readline().split()))
        
        # Read the map itself
        grid = []
        for line in file:
            row = []
            for item in line.split():
                if item == 'X':
                    row.append('X')  # Keep 'X' as is
                else:
                    row.append(int(item))
            grid.append(row)
        
    return rows, cols, start, end, grid

rows, cols, start, end, grid = read_map(mapgrid)

def bfs(graph, start, end):
    queue = deque([start])  # Initialize the queue with the start node
    visited = set()  # Initialize an empty set to keep track of visited nodes
    parent = {}  # Keep track of parent nodes to reconstruct the path

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # Loop until the queue is empty
    while queue:
        current_node = queue.popleft()  # Dequeue the current node

        if current_node == end:  # Check if we've reached the end node
            break

        # Explore neighbors
        for dx, dy in directions:
            neighbor = (current_node[0] + dx, current_node[1] + dy)
            if 0 <= neighbor[0] < len(graph) and 0 <= neighbor[1] < len(graph[0]):
                if graph[neighbor[0]][neighbor[1]] != 'X' and neighbor not in visited:
                    queue.append(neighbor)  # Enqueue the neighbor if it's valid and not visited
                    visited.add(neighbor)  # Mark the neighbor as visited
                    parent[neighbor] = current_node  # Record the parent node for path reconstruction

    # Reconstruct the path from end to start
    path = []
    current_node = end
    while current_node != start:
        path.append(current_node)
        current_node = parent[current_node]
    path.append(start)
    path.reverse()

    return path
    
start_node = (start[0]-1, start[1]-1)
end_node = (end[0]-1, end[1]-1)

path = bfs(grid, start_node, end_node)

if path:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) == start_node or (i, j) == end_node:
                print('*', end=' ')
            elif (i, j) in path:
                print('*', end=' ')
            else:
                print(grid[i][j], end=' ')
        print()  
else:
    print("null")



# def ucs (rows,cols,start,end,grid):
#     return

# def astar (rows,cols,start,end,grid):
#     return





# if alg == "bfs":
#     bfs(rows, cols, start, end, grid)
# elif alg == "ucs":
#     ucs(rows, cols, start, end, grid)
# elif alg == "astar":
#     astar(rows, cols, start, end, grid)
# else:
#     print("null")
