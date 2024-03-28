import sys

map_size = sys.argv[1]

print(map_size)


# def read_map(filename):

#     with open(filename, 'r') as file:
#         # Read map size
#         rows, cols = map(int, file.readline().split())
        
#         # Read start and end positions
#         start = tuple(map(int, file.readline().split()))
#         end = tuple(map(int, file.readline().split()))
        
#         # Read the map itself
#         grid = [list(map(int, line.split())) for line in file]
        
#     return rows, cols, start, end, grid