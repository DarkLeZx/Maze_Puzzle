import tkinter as tk
from generate_maze import generate_maze
from astar import astar

def draw_maze(canvas, maze, path=None):
    cell_size = 20
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            fill = "white" if cell == 0 else "black"
            canvas.create_rectangle(x * cell_size, y * cell_size,
                                    (x + 1) * cell_size, (y + 1) * cell_size,
                                    fill=fill)
    if path:
        for (x, y) in path:
            canvas.create_rectangle(x * cell_size, y * cell_size,
                                    (x + 1) * cell_size, (y + 1) * cell_size,
                                    fill="blue")

def run():
    maze = generate_maze(11, 11)
    path = astar(maze, (1, 1), (9, 9))
    
    root = tk.Tk()
    canvas = tk.Canvas(root, width=220, height=220)
    canvas.pack()
    draw_maze(canvas, maze, path)
    root.mainloop()

if __name__ == "__main__":
    run()
