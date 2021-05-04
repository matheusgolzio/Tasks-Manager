from tkinter import *
from mysql.connector import connect


root = Tk()


class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.widgets()
        self.root.mainloop()

    
    def tela(self):
        self.root.title("Tasks Manager")
        self.root.resizable(False, False)
        self.root.geometry("1280x620")
    
    
    def widgets(self):
        # Name of the task
        self.name_label = Label(self.root, text="Name of the Task", font=("Sans-serif", 20))
        self.name_label.place(relx=0.01, rely=0.01)

        self.name_entry = Entry(self.root, bd=4)
        self.name_entry.place(relx=0.19, rely=0.025, relwidth=0.2)

        # Description of the task
        self.desc_label = Label(self.root, text="Description of the Task", font=("Sans-serif", 20))
        self.desc_label.place(relx=0.01, rely=0.13)

        self.desc_entry = Entry(self.root, bd=4)
        self.desc_entry.place(relx=0.25, rely=0.15, relwidth=0.2)

        # Urgency
        self.urgency_label = Label(self.root, text="Urgency", font=("Sans-serif", 20))
        self.urgency_label.place(relx=0.01, rely=0.22)

        self.urgency = StringVar(self.root)
        self.urgency.set("Low") # default value

        self.optionmenu = OptionMenu(self.root, self.urgency, "Low", "Medium", "High")
        self.optionmenu.place(relx=0.10, rely=0.23)

        # Date
        self.date_label = Label(self.root, text="Date", font=("Sans-serif", 20))
        self.date_label.place(relx=0.01, rely=0.325)

        self.date_entry = Entry(self.root, bd=4)
        self.date_entry.place(relx=0.1, rely=0.34)


Application()
