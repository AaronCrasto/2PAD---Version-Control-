import tkinter as tk
from tkinter import ttk
import random

prefix = '#'

def clearitem():
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    Item_combobox.delete(0, tk.END)
    Quantity_spinbox.delete(0, tk.END)
    receipt_entry.delete(0, tk.END)
def add_item():
    FirstName = first_name_entry.get()
    LastName = last_name_entry.get()
    Item = Item_combobox.get()
    Quantity = int(Quantity_spinbox.get())
    ReceiptNumber =  prefix + str(random.randrange(100,10000))
    data_load = [FirstName, LastName, Item, Quantity, ReceiptNumber]
    tree.insert('',0, values= data_load)

def delete():
    selected_item = tree.selection()[0]
    tree.delete(selected_item)



window = tk.Tk()
window.title("Julie's Party Hire")

frame = tk.Frame(window)
frame.pack(padx=20, pady=10)

first_name_label= tk.Label(frame, text="First Name")
first_name_label.grid(row=0,column=0)
last_name_label= tk.Label(frame, text="Last Name")
last_name_label.grid(row=0,column=1)

first_name_entry= tk.Entry(frame)
last_name_entry= tk.Entry(frame)
first_name_entry.grid(row=1,column=0)
last_name_entry.grid(row=1,column=1)

Item_Label= tk.Label(frame, text="Item Hired")
Item_combobox = ttk.Combobox(frame, values=['Balloons','Party Hat','Tables', 'Chairs'])
Item_Label.grid(row=0,column=2)
Item_combobox.grid(row=1, column=2)

Quantity_label = tk.Label(frame, text="Quantity Hired")
Quantity_label.grid(row=2, column =0)
Quantity_spinbox = tk.Spinbox(frame, from_=0, to=100)
Quantity_spinbox.grid(row=3, column=0)


receipt_label = tk.Label(frame, text="Receipt Number")
receipt_label.grid(row=2, column = 2)
receipt_entry = tk.Entry(frame,state="readonly")
receipt_entry.grid(row=3, column=2)


columns = ('FirstName', 'LastName', 'Item', 'Quantity', 'ReceiptNumber')
tree =ttk.Treeview(frame, columns=columns, show="headings")
tree.heading("FirstName", text='First Name')
tree.heading('LastName', text='Last Name')
tree.heading('Item', text='Item')
tree.heading('Quantity', text='Quantity')
tree.heading('ReceiptNumber', text='Receipt Number')

tree.grid(row=5, column =0, columnspan=3 , padx=20, pady=10)

add_receipt_button =tk.Button(frame, text ="Add Receipt", command = add_item)
add_receipt_button.grid(row=6, column=0, columnspan=3, sticky='news', padx=20, pady=5)
delete_receipt_button = tk.Button(frame, text="Delete Receipt", command= delete)
delete_receipt_button.grid(row=7, column=0, columnspan=3, sticky="news", padx=20, pady=5)


clear_button = tk.Button(frame,text ="Reset", command = clearitem)
clear_button.grid(row=3, column=1, sticky = 'news')
window.configure()



window.mainloop()