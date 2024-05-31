import tkinter as tk
from generate_maze import generate_maze
from astar import astar

def draw_maze(canvas, maze, path=None, current=None, open_list=None):
    cell_size = 20
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            fill = "white" if cell == 0 else "black"
            canvas.create_rectangle(x * cell_size, y * cell_size,
                                    (x + 1) * cell_size, (y + 1) * cell_size,
                                    fill=fill)
    if open_list:
        for (x, y) in open_list:
            canvas.create_rectangle(x * cell_size, y * cell_size,
                                    (x + 1) * cell_size, (y + 1) * cell_size,
                                    fill="lightgreen")
    if path:
        for (x, y) in path:
            canvas.create_rectangle(x * cell_size, y * cell_size,
                                    (x + 1) * cell_size, (y + 1) * cell_size,
                                    fill="blue")
    if current:
        x, y = current
        canvas.create_rectangle(x * cell_size, y * cell_size,
                                (x + 1) * cell_size, (y + 1) * cell_size,
                                fill="yellow")

def run():
    maze = generate_maze(11, 11)
    start, end = (1, 1), (9, 9)
    astar_gen = astar(maze, start, end)

    root = tk.Tk()
    canvas = tk.Canvas(root, width=220, height=220)
    canvas.pack()

    def update():
        try:
            grid, position, status = next(astar_gen)
            if status == "current":
                draw_maze(canvas, maze, current=position)
            elif status == "open":
                draw_maze(canvas, maze, open_list=[position])
            elif status == "path":
                draw_maze(canvas, maze, path=position)
                return
            root.after(100, update)
        except StopIteration:
            return

    draw_maze(canvas, maze)
    root.after(100, update)
    root.mainloop()

if __name__ == "__main__":
    run()
