from window import Window
from line import Point
from cell import Cell

def main():
    win = Window(800, 600)
    cell1 = Cell(win)
    cell1.has_left_wall = False
    cell2 = Cell(win)
    cell2.has_top_wall = False
    cell3 = Cell(win)
    cell3.has_bottom_wall = False
    cell4 = Cell(win)
    cell4.has_right_wall = False
    cell1.draw(Point(100, 100), Point(150, 150))
    cell2.draw(Point(200, 100), Point(250, 150))
    cell3.draw(Point(300, 100), Point(350, 150))
    cell4.draw(Point(400, 100), Point(450, 150))
    cell1.draw_move(cell2)
    cell3.draw_move(cell4, True)
    win.wait_for_close()

if __name__ == "__main__":
    main()
