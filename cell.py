from line import Point, Line

class Cell:
    def __init__(self, window):
        self.__win = window
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__tl = None
        self.__bl = None
        self.__tr = None
        self.__br = None

    def draw(self, point_tl, point_br, color = "black"):
        self.__tl = Point(point_tl.x, point_tl.y)
        self.__bl = Point(point_tl.x, point_br.y)
        self.__tr = Point(point_br.x, point_tl.y)
        self.__br = Point(point_br.x, point_br.y)
        if self.has_left_wall:
            self.__win.draw_line(Line(self.__bl, self.__tl))
        if self.has_top_wall:
            self.__win.draw_line(Line(self.__tl, self.__tr))
        if self.has_right_wall:
            self.__win.draw_line(Line(self.__tr, self.__br))
        if self.has_bottom_wall:
            self.__win.draw_line(Line(self.__br, self.__bl))

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
        self.__win.draw_line(Line(self.get_center(), to_cell.get_center()), color)
