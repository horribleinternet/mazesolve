from line import Point, Line

class Cell:
    def __init__(self, window = None, back_color = "white"):
        self.__win = window
        self.back_color = back_color
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__tl = None
        self.__bl = None
        self.__tr = None
        self.__br = None
        self.visited = False

    def draw(self, x1, y1, x2, y2, color = "black"):
        self.__tl = Point(x1, y1)
        self.__bl = Point(x1, y2)
        self.__tr = Point(x2, y1)
        self.__br = Point(x2, y2)
        if self.__win is None:
            return
        self.__win.draw_line(Line(self.__bl, self.__tl), color if self.has_left_wall else self.back_color)
        self.__win.draw_line(Line(self.__tl, self.__tr), color if self.has_top_wall else self.back_color)
        self.__win.draw_line(Line(self.__tr, self.__br), color if self.has_right_wall else self.back_color)
        self.__win.draw_line(Line(self.__br, self.__bl), color if self.has_bottom_wall else self.back_color)

    def get_center(self):
        if self.__tl is None or self.__br is None:
            return None
        return Point((self.__tl.x + self.__br.x) // 2, (self.__tl.y + self.__br.y) // 2  )
    
    def draw_move(self, to_cell, undo = False):
        color = None
        if undo:
            color = "gray"
        else:
            color = "red"
        if self.__win is not None:
            self.__win.draw_line(Line(self.get_center(), to_cell.get_center()), color)
