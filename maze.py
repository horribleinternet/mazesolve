import time
import random
from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None, seed = None, color = "black", anim_sleep = 0.05):
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
        if seed is not None:
            random.seed(seed)
        self.__create_cells()

    def __create_cells(self):
        self.__cells = [[Cell(self.win) for row in range(self.num_rows)] for col in range(self.num_cols)]
        for i in range(len(self.__cells)):
            for j in range(len(self.__cells[0])):
                self.__draw_cell(i, j)
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)

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

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        adjacency = self.__get_visitable(i, j)
        while len(adjacency) > 0:
            key, value = list(adjacency.items())[random.randrange(len(adjacency))]
            self.__remove_walls(i, j, *value, key)
            self.__draw_cell(*value)
            self.__break_walls_r(*value)
            adjacency = self.__get_visitable(i, j)
    
    def __get_visitable(self, i, j):
        adjacent = {}
        if j > 0 and j < self.num_rows and not self.__cells[i][j-1].visited:
            adjacent[0] = (i, j-1)
        if i >= 0 and i < self.num_cols - 1 and not self.__cells[i+1][j].visited:
            adjacent[1] = (i+1, j)
        if j >= 0 and j < self.num_rows - 1 and not self.__cells[i][j+1].visited:
            adjacent[2] = (i, j+1)
        if i > 0 and i < self.num_cols and not self.__cells[i-1][j].visited:
            adjacent[3] = (i-1, j)
        return adjacent

    def __remove_walls(self, i1, j1, i2, j2, orientation):
        match orientation:
            case 0:
                self.__cells[i1][j1].has_top_wall = False
                self.__cells[i2][j2].has_bottom_wall = False
            case 1:
                self.__cells[i1][j1].has_right_wall = False
                self.__cells[i2][j2].has_left_wall = False
            case 2:
                self.__cells[i1][j1].has_bottom_wall = False
                self.__cells[i2][j2].has_top_wall = False
            case 3:
                self.__cells[i1][j1].has_left_wall = False
                self.__cells[i2][j2].has_right_wall = False
