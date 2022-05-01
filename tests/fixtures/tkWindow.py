import tkinter as tk
from multiprocessing import Process, Queue


async def showInput() -> str:
    q: Queue = Queue()

    class Application(tk.Frame):
        def __init__(self, master=None):
            super().__init__(master)
            self.pack()
            self.createWidgets()

        def createWidgets(self):
            self.label = tk.Label(self, text="input:")
            self.entry = tk.Entry(self)
            self.button = tk.Button(self, text="OK")

            self.label.pack(side="left")
            self.entry.pack(side="left")
            self.button.pack(side="left")
            self.button.bind("<ButtonRelease>", self.onClickOK)

        def onClickOK(self, *args):
            q.put(self.entry.get())

    app = Application(master=tk.Tk())
    app.mainloop()
    yield q.get()


if __name__ == '__main__':
    showInput()
