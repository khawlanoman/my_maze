import random

def dfs(maze, width, height, start, block_42):
    stack = [start]
    visited = set()
    visited.add(start)

    while stack:
        current_row, current_col = stack[-1]

        # find all unvisited neighbors
        neighbors = []
        directions = {'N': (-1,0), 'S':(1,0), 'E':(0,1), 'W':(0,-1)}

        for direction, (row_offset, col_offset) in directions.items():
            neighbor_row = current_row + row_offset
            neighbor_col = current_col + col_offset

            if 0 <= neighbor_row < height and 0 <= neighbor_col < width:
                if (neighbor_row, neighbor_col) not in visited and (neighbor_row, neighbor_col) not in block_42:
                    neighbors.append((direction, (neighbor_row, neighbor_col)))

        if neighbors:
            direction, (neighbor_row, neighbor_col) = random.choice(neighbors)

            # remove wall between current and neighbor
            if direction == 'N':
                maze[current_row][current_col].n = 0
                maze[neighbor_row][neighbor_col].s = 0
            elif direction == 'S':
                maze[current_row][current_col].s = 0
                maze[neighbor_row][neighbor_col].n = 0
            elif direction == 'E':
                maze[current_row][current_col].e = 0
                maze[neighbor_row][neighbor_col].w = 0
            elif direction == 'W':
                maze[current_row][current_col].w = 0
                maze[neighbor_row][neighbor_col].e = 0

            visited.add((neighbor_row, neighbor_col))
            stack.append((neighbor_row, neighbor_col))
        else:
            stack.pop()