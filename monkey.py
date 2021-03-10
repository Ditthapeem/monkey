import tkinter as tk
import tkinter.ttk as ttk

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 500


class MonkeyGame(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.grid(sticky="NEWS")
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self, borderwidth=0, width=CANVAS_WIDTH,
                                height=CANVAS_HEIGHT, highlightthickness=0)
        self.canvas.grid(sticky='NEWS')

        self.banana_image = tk.PhotoImage(file=r'C:/Work/Ske Sem2 2564/Computer Programming II 01219116/Lesson/Week 7/monkey/Banana2.png')
        self.banana = self.canvas.create_image(100, 100, image=self.banana_image)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Monkey Game")

    root.resizable(False, False)
    app = MonkeyGame(root)
    root.mainloop()

