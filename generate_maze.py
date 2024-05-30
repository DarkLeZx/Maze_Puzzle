import random
import csv

def generate_maze(width, height):
    maze = [[1 for _ in range(width)] for _ in range(height)]
    
    def carve_passages_from(x, y):
        directions = [(x - 2, y), (x + 2, y), (x, y - 2), (x, y + 2)]
        random.shuffle(directions)
        
        for (nx, ny) in directions:
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 1:
                maze[ny][nx] = 0
                maze[ny + (y - ny) // 2][nx + (x - nx) // 2] = 0
                carve_passages_from(nx, ny)
    
    maze[1][1] = 0
    carve_passages_from(1, 1)
    return maze

def export_maze_to_csv(maze, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(maze)

# Contoh penggunaan fungsi
if __name__ == "__main__":
    maze = generate_maze(11, 11)
    export_maze_to_csv(maze, 'maze.csv')