import sys

map_name = sys.argv[1]

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

rows, cols, start, end, grid = read_map(map_name)

print("Map dimensions:", rows, "rows x", cols, "columns")
print("Start position:", start)
print("End position:", end)
print("Grid:")
for row in grid:
    print(row)