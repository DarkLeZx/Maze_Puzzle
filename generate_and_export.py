from generate_maze import generate_maze, export_maze_to_csv

def generate_multiple_mazes_and_export():
    sizes = [(11, 11), (15, 15), (21, 21), (25, 25)]
    for i, (width, height) in enumerate(sizes):
        maze = generate_maze(width, height)
        filename = f'maze_{i + 1}.csv'
        export_maze_to_csv(maze, filename)
        print(f'Maze {i + 1} saved as {filename}')

if __name__ == "__main__":
    generate_multiple_mazes_and_export()