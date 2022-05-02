import tkinter as tk
from multiprocessing import Process, Queue


class Application(tk.Frame):
    def __init__(self, master, q: Queue):
        super().__init__(master)
        self.pack()
        self.createWidgets()
        self.q = q

    def createWidgets(self):
        self.label = tk.Label(self, text="input:")
        self.entry = tk.Entry(self)
        self.button = tk.Button(self, text="OK")

        self.label.pack(side="left")
        self.entry.pack(side="left")
        self.button.pack(side="left")
        self.button.bind("<ButtonRelease>", self.onClickOK)

    def onClickOK(self, *args):
        inputValue = self.entry.get()
        self.q.put(inputValue)
        self.quit()


def showInput() -> Queue:
    q: Queue = Queue()
    Process(target=__workload, args=(q,)).start()
    return q


def __workload(q: Queue):
    global Application
    app = Application(tk.Tk(), q)
    app.mainloop()
