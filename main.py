from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from mysql.connector import connect


root = Tk()


class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.widgets()
        self.select_list()
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

        # Delete
        self.id_label = Label(self.root, text="ID", font=("Sans-serif", 20))
        self.id_label.place(relx=0.7, rely=0.01)

        self.id_entry = Entry(self.root, bd=4)
        self.id_entry.place(relx=0.75, rely=0.017)

        self.delete_button = Button(self.root, bd=4, text="Delete", command=self.delete_task)
        self.delete_button.place(relx=0.87, rely=0.015, relwidth=0.1)

        # Edit a item
        self.id_label_edit = Label(self.root, text="ID", font=("Sans-serif", 20))
        self.id_label_edit.place(relx=0.53, rely=0.17)

        self.id_entry_edit = Entry(self.root, bd=4)
        self.id_entry_edit.place(relx=0.57, rely=0.18)


        self.edit_label = Label(self.root, text="Edit", font=("Sans-serif", 20))
        self.edit_label.place(relx=0.7, rely=0.17)

        self.edit_entry = Entry(self.root, bd=4)
        self.edit_entry.place(relx=0.75, rely=0.18)

        self.edit_select = StringVar(self.root)
        self.edit_select.set("name")
        
        self.optionmenu_edit = OptionMenu(self.root, self.edit_select, "name", "description", "urgency", "date")
        self.optionmenu_edit.place(relx=0.85, rely=0.17)

        self.update_button = Button(self.root, text="Update", bd=4, command=self.edit_task)
        self.update_button.place(relx=0.93, rely=0.17)

        # Save
        self.save_button = Button(self.root, text="Save Task", bd=4, command=self.save_task)
        self.save_button.place(relx=0.01, rely=0.42, relwidth=0.13)

        # TreeView
        self.listTask = ttk.Treeview(self.root, height=3,
                                     column=("col1", "col2", "col3", "col4", "col5"))
        self.listTask.heading("#0", text="")
        self.listTask.heading("#1", text="ID")
        self.listTask.heading("#2", text="Name")
        self.listTask.heading("#3", text="Description")
        self.listTask.heading("#4", text="Urgency")
        self.listTask.heading("#5", text="Date")

        self.listTask.column("#0", width=1)
        self.listTask.column("#1", width=50)
        self.listTask.column("#2", width=200)
        self.listTask.column("#3", width=125)
        self.listTask.column("#4", width=125)
        self.listTask.column("#5", width=125)
        self.listTask.place(relx=0, rely=0.5, relwidth=0.98, relheight=0.5)

        self.scroolList = Scrollbar(self.root, orient='vertical')
        self.listTask.configure(yscroll=self.scroolList.set)
        self.scroolList.place(relx=0.98, rely=0.5, relwidth=0.02, relheight=0.5)
    

    def clear_task_entry(self):
        self.name_entry.delete(0, END)
        self.desc_entry.delete(0, END)
        self.date_entry.delete(0, END)
    

    def delete_task(self):
        self.conection_database = connect(
            host="localhost",
            port=3306,
            user="root",
            passwd="password",
            database="tasks_manager"
        )

        self.cursor = self.conection_database.cursor()
        self.cursor.execute(f"DELETE FROM tasks WHERE id = {self.id_entry.get()}")
        messagebox.showinfo("Task Deleted", "The task was deleted from the table sucessfully!")
        self.select_list()
        self.conection_database.commit()
    

    def select_list(self):
        self.listTask.delete(*self.listTask.get_children())
        self.conection_database = connect(
            host="localhost",
            port=3306,
            user="root",
            passwd="password",
            database="tasks_manager"
        )

        self.cursor = self.conection_database.cursor()

        self.cursor.execute(""" SELECT id, name, description, urgency, date_of_task FROM tasks; """)
        lista = self.cursor.fetchall()
        for i in lista:
            self.listTask.insert("", END, values=i)
        
        self.conection_database.commit()
    

    def edit_task(self):
        self.conection_database = connect(
            host="localhost",
            port=3306,
            user="root",
            passwd="password",
            database="tasks_manager"
        )

        self.cursor = self.conection_database.cursor()

        self.cursor.execute(f"""UPDATE tasks set {self.edit_select.get()} = '{self.edit_entry.get()}' WHERE id = '{self.id_entry_edit.get()}'""")
        self.select_list()
        messagebox.showinfo("Updated", "The task was updated.")
        self.conection_database.commit()
    

    def save_task(self):
        self.conection = connect(
            host="localhost",
            port=3306,
            user="root",
            passwd="password"
        )

        self.cursor = self.conection.cursor()

        self.cursor.execute("CREATE DATABASE IF NOT EXISTS tasks_manager")

        self.conection.commit()

        self.conection_database = connect(
            host="localhost",
            port=3306,
            user="root",
            passwd="password",
            database="tasks_manager"
        )

        self.cursor = self.conection_database.cursor()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
            id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
            name VARCHAR(100) NOT NULL,
            description VARCHAR(500),
            urgency VARCHAR(10),
            date_of_task VARCHAR(20)
        );""")

        self.name = self.name_entry.get()
        self.desc = self.desc_entry.get()
        self.urgency = self.urgency.get()
        self.date_of_task = self.date_entry.get()

        self.cursor.execute(f"""INSERT INTO tasks (name, description, urgency, date_of_task)
        VALUES ('{self.name}', '{self.desc}', '{self.urgency}', '{self.date_of_task}')""")
        self.conection_database.commit()
        self.clear_task_entry()
        messagebox.showinfo("Task Saved", "The Task was saved sucessfully!")
        self.select_list()
        self.cursor.commit()


Application()
