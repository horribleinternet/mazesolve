from window import Window
from line import Point, Line

def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(100, 100), Point(700, 500)), "black")
    win.wait_for_close()

if __name__ == "__main__":
    main()
