# Modules
import tkinter as tk # Importing tkinter as tk allows me to acess all the modules within tkinter.
from tkinter import ttk # Importing ttk provides me with acess to additional Tkinter modules and widgets.
import random # Importing random allows me to load the random module which is beneficial later in the program . 
from tkinter import messagebox # Importing messageboxes allows my GUI to have a better user interface and making my program more user friendly.


prefix = '#' # This variable allows me to have a prefix of a hashtag before my receipt number.


original_treeview = [] # This variable represents my starting display of receipts which is obviously nothing.

def clear_receipt(): # This function clears all my entries after a receipt is added to the display.
    first_name_entry.delete(0, tk.END) # This line of code deletes the entry of the users First Name after a receipt is added.
    last_name_entry.delete(0, tk.END)# This line of code deletes the entry of the users Last Name after a receipt is added.
    Item_combobox.delete(0, tk.END) # This line of code deletes the entry of the users choice of Item from the drop down box  after a receipt is added.
    Quantity_spinbox.delete(0, tk.END)# This line of code deletes the entry of the Quantity of an Item a customer has bought after a receipt is added.
def add_receipt(): # This function allows me to add a receipt to my display.
    FirstName = first_name_entry.get() # This line of code allows me to collate the customers information as variables in this case their First Name.
    # Error Proofing.
    if FirstName.isdigit(): # This line of code is to ensure that the user doesn't enter a number instead of their First Name.
        messagebox.showerror(title= "Error", message="Please Enter Your First Name, Not a Number") # This line of code prints an error message if the user uses numbers instead of letters for their First Name.
        return # This loops the code so the input is not added to the grid and re-asks the user for their first name
    if FirstName.isalpha() == False:# This line of code ensures that the user only uses letters and no other characters when entering their First Name.
        messagebox.showwarning(title="Error", message="Please Enter Your First Name")# Prints error message when user uses something other than letters in their entry.
    LastName = last_name_entry.get()# This line of code allows me to collate the customers information as variables in this case their First Name.
    if LastName.isdigit():# This line of code is to ensure that the user doesn't enter a number instead of their Last Name
        messagebox.showerror(title= "Error", message="Please Enter Your Last Name, Not a Number")# This line of code prints an error message if the user uses numbers instead of letters for their Last Name.
        return # This loops the code so the input is not added to the grid and re-asks the user for their Last name
    if LastName.isalpha() == False:# This line of code ensures that the user only uses letters and no other characters when entering their First Name.
        messagebox.showerror(title="Error", message="Please Enter Your Last Name")# Prints error message when user uses something other than letters in their entry.
        return # This loops the code so the input is not added to the grid and re-asks the user for their Last name
    Item = Item_combobox.get()
    Quantity = Quantity_spinbox.get()
    

    if not FirstName or not LastName or not Item or not Quantity:
        messagebox.showerror("Error", "Please fill in all the fields.")
        return
    try:
        Quantity = int(Quantity)
        if int(Quantity) not in range(1,500):
            messagebox.showerror("Invalid Input","Choose and apprpriate number, Range between 1-500")
            return False
        else:
            return True
    except ValueError:
        messagebox.showerror("Error", "Quantity must be an integer")
        return
    Quantity = Quantity_spinbox.get()
    

    ReceiptNumber =  prefix + str(random.randrange(100,10000))
    data_load = [FirstName, LastName, Item, Quantity, ReceiptNumber]
    tree.insert('',0, values= data_load)
    original_treeview.append(data_load)
    clear_receipt()

def delete():
    global original_treeview
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showinfo("Info", "Please select an item to delete.")
        return
    confirm_delete = messagebox.askyesno("Confirmation", "Are you sure want to delete the selected item")
    if not confirm_delete:
        return
    for item in selected_item:
        data = tree.item(item, 'values')
        if data in original_treeview:
            original_treeview.remove(data)
        tree.delete(item)

    messagebox.showinfo("Info", "Item has been deleted successfully")
    
def search():
    global original_treeview
    search_text = search_entry.get().lower()
    search_selection = column_combobox.get()

    if not search_text or not search_selection:
        messagebox.showinfo("Info","Please Enter Something and chose the Classification")
        return
        
    for item in tree.get_children():
        tree.tag_configure(item, background='')

    matching_items = []

    for item in tree.get_children():
        values = tree.item(item, 'values')
        index = columns.index(search_selection)
        if search_text in str(values[index]).lower():
           tree.tag_configure(item, background= '')
           matching_items.append(item)
        else:
            tree.detach(item)

    if not matching_items:
        messagebox.showinfo("Info","No matching results were found")
        return
    if not original_treeview:
        original_treeview = [tree.item(item, 'values') for item in tree.get_children()]
    messagebox.showinfo("Info","Search completed successfully.")
    
def reset_treeview():
    if not  original_treeview:
        messagebox.showinfo("Info", "Nothing to Reset.")
        return
    
    confirm_reset = messagebox.askyesno("Confimration", "Are you sure you want to reset the Treeview")
    if not confirm_reset:
        return
    
    try:
        search_entry.delete(0, tk.END)
        column_combobox.set('')

        tree.delete(*tree.get_children())

        copy_original_treeview = list(original_treeview)
        for data in copy_original_treeview:
            tree.insert('', 'end', values=data)

        

        messagebox.showinfo("Info", "Treeview has been reset successfully.")

    except Exception as e:
        messagebox.showerror("Error","An error has occured")
        return

    #for item in tree.get_children():
        #if item not in search_results:
            #tree.detach(item)

    


    for item in tree.get_children():
        tree.delete(item)
    for data in original_treeview:
        tree.insert('', 'end', values=data)

    original_treeview.clear()
def add_new_item():
    add_menu = tk.Toplevel(window)
    add_menu.title("Add New Item")
    add_menu.geometry("400x200")
    
    add_menu_frame = tk.LabelFrame(add_menu, text="New Item Details")
    add_menu_frame.grid(padx=10, pady=10)

    def valid_input(char):
        return char.isalpha() or char == ""

    search_entry = tk.Entry(add_menu_frame, font=("Helvitica", 18))
    search_entry.grid(padx=20, pady=20)

    item_button = tk.Button(add_menu_frame, text="Add Item", command=lambda: add_to_combobox(search_entry.get()))
    item_button.grid(row=1, column=0, padx=20)
    
    
    def add_to_combobox(user_input): 
        if user_input:
            if user_input.isalpha():   
                Item_combobox['values'] = list(Item_combobox['values']) + [user_input]    
            else:
                messagebox.showerror("Error", "Please only use Alphabetical Character")
            
            add_menu.destroy()

    
    
    

window = tk.Tk()
window.title("Julie's Party Hire")

frame = tk.Frame(window)
frame.pack()#padx=60, pady=50
window.geometry("1280x600")

user_info_frame = tk.LabelFrame(frame)
user_info_frame.grid(       )

first_name_label= tk.Label(frame, text="First Name")
first_name_label.grid(row=0,column=0)
last_name_label= tk.Label(frame, text="Last Name")
last_name_label.grid(row=0,column=1)

first_name_entry= tk.Entry(frame)
last_name_entry= tk.Entry(frame)
first_name_entry.grid(row=1,column=0)
last_name_entry.grid(row=1,column=1)

Item_Label= tk.Label(frame, text="Item Hired")
Item_combobox = ttk.Combobox(frame,state="readonly") 
Item_combobox['values']=['Balloons','Party Hat','Tables', 'Chairs']
Item_Label.grid(row=0,column=2)
Item_combobox.grid(row=1, column=2)


            



Quantity_label = tk.Label(frame, text="Quantity Hired")
Quantity_label.grid(row=0, column =3)
Quantity_spinbox = tk.Spinbox(frame, from_=1, to=500)
Quantity_spinbox.grid(row=1, column=3)

    


#receipt_label = tk.Label(frame, text="Receipt Number")
#receipt_label.grid(row=2, column = 2)
#receipt_entry = tk.Entry(frame,state="readonly")
#receipt_entry.grid(row=3, column=2)


columns = ('FirstName', 'LastName', 'Item', 'Quantity', 'ReceiptNumber')
column_combobox = ttk.Combobox(frame, values = columns, state='readonly')
column_combobox.grid(row =4, column=6, padx=20,pady=5)
column_combobox.set('')
tree =ttk.Treeview(frame, columns=columns, show="headings")
tree.heading("FirstName", text='First Name')
tree.heading('LastName', text='Last Name')
tree.heading('Item', text='Item')
tree.heading('Quantity', text='Quantity')
tree.heading('ReceiptNumber', text='Receipt Number')

tree.grid(row=5, column =0, columnspan=4 , padx=20, pady=10)

add_receipt_button =tk.Button(frame, text ="Add Receipt", command = add_receipt)
add_receipt_button.grid(row=6, column=0, columnspan=4, sticky='news', padx=20, pady=5)
delete_receipt_button = tk.Button(frame, text="Delete Receipt", command= delete)
delete_receipt_button.grid(row=7, column=0, columnspan=4, sticky="news", padx=20, pady=5)


CreateItem = tk.Button(frame,text ="Add New Item...", command = add_new_item)
CreateItem.grid(row=8, column=0, columnspan=4,sticky = 'news', padx=20, pady=5)
window.configure()

search_entry = tk.Entry(frame)
search_entry.grid(row=4, column=0, columnspan=3,sticky="news", padx=20, pady=5)
search_button = tk.Button(frame, text='Search', command= search)
search_button.grid(row= 4, column =3,padx=20, pady=5)
reset_button = tk.Button(frame, text="Reset", command= reset_treeview)
reset_button.grid(row =9,column=0, columnspan=4,sticky = 'news', padx=20, pady=5)



window.mainloop()