from tkinter import *
from mysql.connector import connect


root = Tk()


class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.root.mainloop()

    
    def tela(self):
        self.root.title("Tasks Manager")
        self.root.resizable(False, False)
        self.root.geometry("1280x620")


Application()
