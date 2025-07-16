import time
from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None, color = "black", anim_sleep = 0.05):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.anim_sleep = anim_sleep
        self.color = color
        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        self.__cells = [[Cell(self.win) for row in range(self.num_rows)] for col in range(self.num_cols)]
        for i in range(len(self.__cells)):
            for j in range(len(self.__cells[0])):
                self.__draw_cell(i, j)
        self.__break_entrance_and_exit()

    def __draw_cell(self, i, j):
        if (i < 0):
            i = self.num_cols + i
        if (j < 0):
            j = self.num_rows + j
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        self.__cells[i][j].draw(x1, y1, x1 + self.cell_size_x, y1 + self.cell_size_y, self.color)
        self.__animate()
    
    def __animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(self.anim_sleep)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[-1][-1].has_bottom_wall = False
        self.__draw_cell(-1, -1)
