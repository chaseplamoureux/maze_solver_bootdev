from tkinter import Tk, Canvas

class Window():
    def __init__(self, width, height):
        self.root_widget = Tk()
        self.root_widget.title("Maze Solver Project")
        self.canvas = Canvas(self.root_widget, bg="white", height=height, width=width)
        self.canvas.pack()
        self.running = False
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color="black"):
            line.draw(self.canvas, fill_color)

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.x.x, self.x.y, self.y.x, self.y.y, fill=fill_color, width=2)


