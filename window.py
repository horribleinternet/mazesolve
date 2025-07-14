from tkinter import Tk, BOTH, Canvas
from line import Line

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.root.title = "maze"
        self.canvas = Canvas(height=height, width=width)
        self.canvas.pack()
        self.running = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, color):
        line.draw(self.canvas, color)