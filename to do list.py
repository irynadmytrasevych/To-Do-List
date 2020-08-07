import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.geometry('400x300')
root.title("To do list")

task=[]

def add_task():
    word=enter_field.get()
    if len(word)==0:
        messagebox.showinfo('Empty Entry', 'Enter task name')
    else:
        task.append(word)
        list_upd()
        enter_field.delete(0,'end')

def del_task():
    val=listbox.get(listbox.curselection())
    if val in task:
        task.remove(val)
        list_upd()

def del_all():
    mb=messagebox.askyesno("Are you sure?")
    if mb:
        while(len(task)!=0):
            task.pop()
        list_upd()


def list_upd():
    listbox.delete(0,'end')
    for i in task:
        listbox.insert('end', i)


enter_field = tk.Entry(width=24)
button_add = tk.Button(text="Add task", width=20, command=add_task)
button_del = tk.Button(text="Delete task", width=20, command=del_task)
button_del_all = tk.Button(text="Delete all tasks", width=20, command=del_all)
listbox = tk.Listbox(height=15)
label = tk.Label(text="Enter task title")

label.place(x=50,y=50)
enter_field.place(x=50,y=80)
button_add.place(x=50,y=110)
button_del.place(x=50,y=140)
button_del_all.place(x=50,y=170)
listbox.place(x=220,y=50)

root.mainloop()