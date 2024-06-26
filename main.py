import tkinter as tk
from tkinter import messagebox
from generate_maze import generate_maze
from astar import astar
import time

class MazeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Maze Puzzle")
        
        self.levels = [(11, 11), (15, 15), (21, 21), (25, 25)]
        self.current_level = 0
        self.maze = None
        self.start = (1, 1)
        self.end = None
        self.path = None
        self.start_time = None
        self.iterations = 0
        self.canvas = tk.Canvas(root, width=500, height=500)
        self.canvas.grid(row=0, column=0, rowspan=3, padx=10, pady=10)

        self.create_widgets()
        self.generate_new_maze()

    def create_widgets(self):
        self.control_frame = tk.Frame(self.root, bg="skyblue")
        self.control_frame.grid(row=0, column=1, sticky="n", pady=10, padx=10)

        self.level_var = tk.IntVar(value=self.current_level)
        for i, (width, height) in enumerate(self.levels):
            tk.Radiobutton(self.control_frame, text=f"Level {i+1} ({width}x{height})",
                           variable=self.level_var, value=i, command=self.change_level,
                           bg="skyblue", padx=10).pack(anchor="w")

        tk.Button(self.control_frame, text="Reset Maze", command=self.reset_maze,
                  bg="lightgreen").pack(side="left", padx=10, pady=10)
        tk.Button(self.control_frame, text="Solve Maze", command=self.solve_maze,
                  bg="orange").pack(side="left", padx=10, pady=10)
        self.time_label = tk.Label(self.control_frame, text="Time: 0.00 seconds", bg="skyblue")
        self.time_label.pack(side="left", padx=10, pady=10)

        # Label untuk keterangan warna
        legend_frame = tk.LabelFrame(self.root, text="Color Legend", bg="skyblue")
        legend_frame.grid(row=1, column=1, sticky="nw", padx=10, pady=10)
        tk.Label(legend_frame, text="Green: Start", bg="skyblue", fg="green").pack(anchor="w")
        tk.Label(legend_frame, text="Red: Goal", bg="skyblue", fg="red").pack(anchor="w")
        tk.Label(legend_frame, text="Yellow: Current", bg="skyblue", fg="yellow").pack(anchor="w")
        tk.Label(legend_frame, text="Light Green: Open List", bg="skyblue", fg="lightgreen").pack(anchor="w")
        tk.Label(legend_frame, text="Blue: Path", bg="skyblue", fg="blue").pack(anchor="w")

        # Text area untuk menampilkan proses algoritma
        self.text_area_process = tk.Text(self.root, width=40, height=10, wrap=tk.WORD)
        self.text_area_process.grid(row=0, column=2, padx=10, pady=10)
        self.text_area_process.tag_config("current", foreground="yellow", background="black")
        self.text_area_process.tag_config("open", foreground="lightgreen", background="black")
        self.text_area_process.tag_config("path", foreground="blue", background="black")

        # Text area untuk menampilkan hasil akhir
        self.text_area_result = tk.Text(self.root, width=40, height=10, wrap=tk.WORD)
        self.text_area_result.grid(row=1, column=2, padx=10, pady=10)

    def change_level(self):
        self.current_level = self.level_var.get()
        self.generate_new_maze()

    def generate_new_maze(self):
        width, height = self.levels[self.current_level]
        self.maze = generate_maze(width, height)
        self.end = (width - 2, height - 2)
        self.path = None
        self.draw_maze()
        self.time_label.config(text="Time: 0.00 seconds")
        self.text_area_process.delete(1.0, tk.END)
        self.text_area_result.delete(1.0, tk.END)
        self.iterations = 0  # Reset iterations

    def reset_maze(self):
        self.generate_new_maze()

    def solve_maze(self):
        self.start_time = time.time()
        self.path = None
        self.draw_maze()
        self.a_star_generator = astar(self.maze, self.start, self.end)
        self.root.after(100, self.step)

    def step(self):
        try:
            grid, position, status = next(self.a_star_generator)
            self.iterations += 1  # Increment iterations
            if status == "current":
                self.draw_maze()
                self.highlight_position(position, "yellow")
            elif status == "open":
                self.highlight_position(position, "lightgreen")
            elif status == "path":
                self.path = position
                self.draw_maze()
                end_time = time.time()
                elapsed_time = end_time - self.start_time
                self.time_label.config(text=f"Time: {elapsed_time:.2f} seconds")
                self.display_final_path()
                messagebox.showinfo("Puzzle Completed", "Puzzle has been solved!")
                return
            self.update_text_area(status, position)
            self.root.after(100, self.step)
        except StopIteration:
            messagebox.showerror("Error", "No path found!")

    def draw_maze(self):
        self.canvas.delete("all")
        width, height = self.levels[self.current_level]
        cell_size = min(500 // width, 500 // height)
        
        for y in range(height):
            for x in range(width):
                color = "white" if self.maze[y][x] == 0 else "black"
                self.canvas.create_rectangle(x * cell_size, y * cell_size,
                                             (x + 1) * cell_size, (y + 1) * cell_size, fill=color)

        self.highlight_position(self.start, "green")
        self.highlight_position(self.end, "red")

        if self.path:
            for (x, y) in self.path:
                self.canvas.create_rectangle(x * cell_size, y * cell_size,
                                             (x + 1) * cell_size, (y + 1) * cell_size, fill="blue")

    def highlight_position(self, position, color):
        width, height = self.levels[self.current_level]
        cell_size = min(500 // width, 500 // height)
        x, y = position
        self.canvas.create_rectangle(x * cell_size, y * cell_size,
                                     (x + 1) * cell_size, (y + 1) * cell_size, fill=color)

    def update_text_area(self, status, position):
        if status == "current":
            self.text_area_process.insert(tk.END, "Current position: {}\n".format(position), "current")
        elif status == "open":
            self.text_area_process.insert(tk.END, "Added to open list: {}\n".format(position), "open")
        elif status == "path":
            self.text_area_process.insert(tk.END, "Path found: {}\n".format(position), "path")

    def display_final_path(self):
        self.text_area_result.delete(1.0, tk.END)
        self.text_area_result.insert(tk.END, "Final path:\n")
        for step in self.path:
            self.text_area_result.insert(tk.END, "{}\n".format(step))
        self.text_area_result.insert(tk.END, "\nTotal iterations: {}\n".format(self.iterations))

def main():
    root = tk.Tk()
    app = MazeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
