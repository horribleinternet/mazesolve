from window import Window
from line import Point
from cell import Cell
from maze import Maze

def main():
    cell_size = 50
    rows = 15
    cols = 20
    win = Window(cols*cell_size, rows*cell_size)
    # cell1 = Cell(win)
    # cell1.has_left_wall = False
    # cell2 = Cell(win)
    # cell2.has_top_wall = False
    # cell3 = Cell(win)
    # cell3.has_bottom_wall = False
    # cell4 = Cell(win)
    # cell4.has_right_wall = False
    # cell1.draw(100, 100, 150, 150)
    # cell2.draw(200, 100, 250, 150)
    # cell3.draw(300, 100, 350, 150)
    # cell4.draw(400, 100, 450, 150)
    # cell1.draw_move(cell2)
    # cell3.draw_move(cell4, True)
    maze = Maze(1, 1, rows, cols, cell_size, cell_size, win )
    win.wait_for_close()

if __name__ == "__main__":
    main()
