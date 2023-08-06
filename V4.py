# Modules
import tkinter as tk # Importing tkinter as tk allows me to acess all the modules within tkinter.
from tkinter import ttk # Importing ttk provides me with acess to additional Tkinter modules and widgets.
import random # Importing random allows me to load the random module which is beneficial later in the program . 
from tkinter import messagebox # Importing messageboxes allows my GUI to have a better user interface and making my program more user friendly.

MAX_QUANTITY = 500
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
        return # This loops the code so the input is not added to the grid and re-asks the user for their first name.
    if FirstName.isalpha() == False:# This line of code ensures that the user only uses letters and no other characters when entering their First Name.
        messagebox.showwarning(title="Error", message="Please Enter Your First Name")# Prints error message when user uses something other than letters in their entry.
    LastName = last_name_entry.get()# This line of code allows me to collate the customers information as variables in this case their First Name.
    if LastName.isdigit():# This line of code is to ensure that the user doesn't enter a number instead of their Last Name.
        messagebox.showerror(title= "Error", message="Please Enter Your Last Name, Not a Number")# This line of code prints an error message if the user uses numbers instead of letters for their Last Name.
        return # This loops the code so the input is not added to the grid and re-asks the user for their Last name.
    if LastName.isalpha() == False:# This line of code ensures that the user only uses letters and no other characters when entering their First Name.
        messagebox.showerror(title="Error", message="Please Enter Your Last Name")# Prints error message when user uses something other than letters in their entry.
        return # This loops the code so the input is not added to the grid and re-asks the user for their Last name.
    Item = Item_combobox.get() # This line of code allows me to collate the customers information as variables in this case the item they have purchased.
    Quantity = Quantity_spinbox.get() # This line of code allows me to collate the customers information as variables in this case the amount of the item they have purchased.
    

    if not FirstName or not LastName or not Item or not Quantity: # This line of code ensures that none of the entries are left empty.
        messagebox.showerror("Error", "Please fill in all the fields.") # This line of code prints an error message if any entry has not been filled.
        return # This loops the code so the input is not added to the grid and asks the user to fill in all the entries .
    try:
        Quantity = int(Quantity) # This ensures that the Quantity is set to an integer.
        if int(Quantity) not in range(1,MAX_QUANTITY+1): # This line of code ensures that the quantity that can be purchased is appropriate hence I chose the range to be between 1 and 500
            messagebox.showerror("Invalid Input","Choose and apprpriate number, Range between 1-500") # This line of code prints an error message if the entry is not within the range of 1 - 500.
            return False # This loops the code so the input is not added to the grid and re-asks the user to fill in the Quantity. 
        else:
            return True # This code breaks the loop if the user choses a quantity within the range.
    except ValueError: # This line of code ensures that user only enters an integer into the Quantity entry.
        messagebox.showerror("Error", "Quantity must be an integer") # # This line of code prints an error message if a non-integer has been used.
        return # This loops the code so the input is not added to the grid and re-asks the user to fill in the Quantity.
    
    

    ReceiptNumber =  prefix + str(random.randrange(100,10000)) # This variable choses a random receipt number for the user when a valid entry is made
    data_load = [FirstName, LastName, Item, Quantity, ReceiptNumber] # This variable is a list of the all the entries collated 
    tree.insert('',0, values= data_load)# This line of code displays the users entry on the GUI
    original_treeview.append(data_load)# This line of code adds the data to the original_treeview list.
    clear_receipt()# This function calls the clear_receipt function which resets the entries after a valid receipt has been added.

def delete(): # This function is used to delete any receipts that are being displayed.
    global original_treeview # This line of code allows me to call the original data list to nay part of the program.
    selected_item = tree.selection()
    if not selected_item: # This line of code ensures the user has selected an item before clicking the delete button
        messagebox.showinfo("Info", "Please select an item to delete.") # This error message is printed if the user doesn't choose a receipt before clicking the delete button.
        return
    confirm_delete = messagebox.askyesno("Confirmation", "Are you sure want to delete the selected item")# This line of code asks the user for confirmation if they want to delete the receipt.
    if not confirm_delete:
        return# If the user says no the code will return back tot the original display.
    for item in selected_item: # This line of code will proceed If the user says yes to delete the receipt. 
        data = tree.item(item, 'values')
        if data in original_treeview:  
            original_treeview.remove(data)# This line of code will delete the data fromt the original data list. 
        tree.delete(item) # This line of code will delete the data from the display.

    messagebox.showinfo("Info", "Item has been deleted successfully") # This message will be printed when the receipt is deleted.
    
def search(): # This function is used if the user wants to search a previous receipt 
    global original_treeview
    search_text = search_entry.get().lower() # This line of code is used to ask information about the receipt. 
    search_selection = column_combobox.get() # This line of code is used to confirm what has the user provided in the search bar.

    if not search_text or not search_selection:# This line of code is to ensure that when searching the user doesn't leave either of these boxes empty.
        messagebox.showinfo("Info","Please Enter Something and chose the Classification")# This message will be displayed if the user leaves any box empty
        return # This will loop the code back to the search bar 
        
    for item in tree.get_children(): # If the user uses valid information in the search bar this code will find the users entry in the display
        tree.tag_configure(item, background='')  # This line of code showcases how the infomration will be displayed 

    matching_items = [] # This variable is used to see whether such an entry exists in the database

    for item in tree.get_children(): # These lines of code is finding the users display depending on the information they have provided eg. Quantity, Item, FirstName e.t.c
        values = tree.item(item, 'values')
        index = columns.index(search_selection)
        if search_text in str(values[index]).lower():
           tree.tag_configure(item, background= '')
           matching_items.append(item)# When the program finds the item it appends it to the matching_items list
        else:
            tree.detach(item)# This line of code separates the searched data from the rest.

    if not matching_items:# This line of code is used if the program cant find a match to the user's search
        messagebox.showinfo("Info","No matching results were found")# This error message is displayed if the search can't be found
        return # If the search isnt found this line of code will loop the program back to the main window.
    if not original_treeview:# If the data is found this line of code will bring to the original treeview.
        original_treeview = [tree.item(item, 'values') for item in tree.get_children()]# This line of code will display the data on the main window treeview.
    messagebox.showinfo("Info","Search completed successfully.")# This message will be displayed to the user if their search was successfull.
    
def reset_treeview(): # This function is used to reset the entries back to the original treeview
    if not  original_treeview: # This line of codie is used f the user clicks the reset button, however the entries are already on the original treeview. 
        messagebox.showinfo("Info", "Nothing to Reset.") # This message will be displayed.
        return # The line of code will loop the program back to the main screen
    
    confirm_reset = messagebox.askyesno("Confimration", "Are you sure you want to reset the Treeview")# This line of code asks the user of confirmation if they want to reset back to the original treeview.
    if not confirm_reset:
        return # If they say no this line of code will loop the program back to the current treeview.
    
    try:
        search_entry.delete(0, tk.END) # If the user clicks yes this line of code resets the search bar.
        column_combobox.set('') # If the user clicks yes this line of code resets the category they were searching in.

        tree.delete(*tree.get_children())# This line of code bring back all the receipts that weren't searched.

        copy_original_treeview = list(original_treeview) # These lines of code ensure that all the entries are displayed on the GUI. 
        for data in copy_original_treeview:
            tree.insert('', 'end', values=data)

        

        messagebox.showinfo("Info", "Treeview has been reset successfully.") # This message is displayed to the user when the Tree view has been reset.

    except Exception as e:
        messagebox.showerror("Error","An error has occured")# However if an error occurs while resetting the treeview this messagebox will be displayed.
        return# This line of code will loop the program to the previous treeview.



    


    for item in tree.get_children(): # These lines of code are ensuring that all the receipts that have been deleted or excluded ealrier aren't involved in the resetted Treeview.
        tree.delete(item)
    for data in original_treeview:
        tree.insert('', 'end', values=data)

    original_treeview.clear()

def add_new_item(): # This function is used if the user wants to add a new item that isnt in the combobox/dropdown menu.
    add_menu = tk.Toplevel(window) # This line of code creates a new window within the main screen.
    add_menu.title("Add New Item")# This line of code sets the title of the new window.
    add_menu.geometry("400x200")# This line of code sets the dimensions for the window.
    
    add_menu_frame = tk.LabelFrame(add_menu, text="New Item Details")# This line of code creates a frame in the window.
    add_menu_frame.grid(padx=10, pady=10)# This line of code sets the size of the frame.

    def valid_input(char): # This function ensures that the entry box to add a new item isn't left empty 
        return char.isalpha() or char == ""

    search_entry = tk.Entry(add_menu_frame, font=("Helvitica", 18)) # This line of code creates the entry box and custom styling for the users new item entry.
    search_entry.grid(padx=20, pady=20) # This line of code sets the size of the entry box.

    item_button = tk.Button(add_menu_frame, text="Add Item", command=lambda: add_to_combobox(search_entry.get()))# This line of code creates the button to add the add the item and set its command.
    item_button.grid(row=1, column=0, padx=20) #  This line of code sets the size of the button.
    
    
    def add_to_combobox(user_input): # This fucntion is used to add the users new item entry into the items list. 
        if user_input:
            if user_input.isalpha(): # This line of code is used to check whether the entry is valis  
                Item_combobox['values'] = list(Item_combobox['values']) + [user_input] # This line of code will add the entry to the items list.    
            else:
                messagebox.showerror("Error", "Please only use Alphabetical Character") # If the users entry is invalid this message will be displayed.
            
            add_menu.destroy() # If the entry is valid this line of code will automatically quit the add item window.

    
    
    

window = tk.Tk() # This line of code creates the main screen of our GUI.
window.title("Julie's Party Hire") # This line of code sets the name of the main screen or window.

frame = tk.Frame(window, bg = "#333333")# This line of code creates the frame of our GUI.
frame.pack()
window.geometry("1280x600")# This line of code sets the name of the main screen or window.

user_info_frame = tk.LabelFrame(frame) # This line of code creates the label frame of our GUI.
user_info_frame.grid()

first_name_label= tk.Label(frame, text="First Name",bg='#333333',fg= 'white') # This line of code creates the label for the First Name of the user. 
first_name_label.grid(row=0,column=0)# This line of code sets the postion of the First Name label on the GUI.
last_name_label= tk.Label(frame, text="Last Name",bg='#333333',fg= 'white') # This line of code creates the label for the Last Name of the user.
last_name_label.grid(row=0,column=1)# This line of code sets the postion of the Last Name label on the GUI.

first_name_entry= tk.Entry(frame)# This line of code creates the entry box for the First Name of the user. 
last_name_entry= tk.Entry(frame)# This line of code creates the entry box for the Last Name of the user. 
first_name_entry.grid(row=1,column=0)# This line of code sets the postion of the First Name entry box  on the GUI.
last_name_entry.grid(row=1,column=1)# This line of code sets the postion of the  Last Name entry box  on the GUI.

Item_Label= tk.Label(frame, text="Item Hired",bg='#333333',fg= 'white')  # This line of code creates the label for the Items List .
Item_combobox = ttk.Combobox(frame,state="readonly") # This line of code creates the combox and makes sure that the user cant add his own item onto the combobox directly.
Item_combobox['values']=['Balloons','Party Hat','Tables', 'Chairs']# This line of code adds some pre-existing options to the item list
Item_Label.grid(row=0,column=2) # This line of code sets the postion of the Items label on the GUI
Item_combobox.grid(row=1, column=2)# This line of code sets the postion of the Items List Combobox  on the GUI.


            



Quantity_label = tk.Label(frame, text="Quantity Hired", bg='#333333', fg= 'white')# This line of code creates the label for the Quantity Hired by the customer.
Quantity_label.grid(row=0, column =3)# This line of code sets the postion of the Quantitylabel on the GUI.
Quantity_spinbox = tk.Spinbox(frame, from_=1, to=500)# This line of code sets creates the spinbox for the Quantity with a range between 1-500.
Quantity_spinbox.grid(row=1, column=3)# This line of code sets the postion of the Quantity Spinbox  on the GUI.
    
columns = ('FirstName', 'LastName', 'Item', 'Quantity', 'ReceiptNumber') # This line of code adds the coloums on the treeview 
column_combobox = ttk.Combobox(frame, values = columns, state='readonly')# This line creates the combobox when searching for a particular keyword.
column_combobox.grid(row =4, column=2,columnspan=2, sticky='ew', padx=20,pady=5)# This line of code sets the position of the combobox
column_combobox.set('')
tree =ttk.Treeview(frame, columns=columns, show="headings") # This line of code creates the treeview
# These lines of code below  are what the headings would be displayed on the treeview
tree.heading("FirstName", text='First Name') 
tree.heading('LastName', text='Last Name')
tree.heading('Item', text='Item')
tree.heading('Quantity', text='Quantity')
tree.heading('ReceiptNumber', text='Receipt Number')

tree.grid(row=5, column =0, columnspan=4 , padx=20, pady=10) # This line of code sets the dimensions and the poistion of the treeview on the GUI

add_receipt_button =tk.Button(frame, text ="Add Receipt", command = add_receipt, bg= "#79AFB8") # This line of code creates a button to add receipt and the function add_receipt from above is called. 
add_receipt_button.grid(row=6, column=0, columnspan=4, sticky='news', padx=20, pady=5) # This line of code sets the size and postion of the add receipts button.
delete_receipt_button = tk.Button(frame, text="Delete Receipt", command= delete, bg="#79AFB8")# This line of code creates a button to delete a receipt  and the function delete from above is called. 
delete_receipt_button.grid(row=7, column=0, columnspan=4, sticky="news", padx=20, pady=5)# This line of code sets the size and postion of the delete receipts button.


CreateItem = tk.Button(frame,text ="Add New Item...", command = add_new_item, bg="#79AFB8")# This line of code creates a button to create the new item on the second window and the function add_new_item from above is called. 
CreateItem.grid(row=8, column=0, columnspan=4,sticky = 'news', padx=20, pady=5)# This line of code sets the size and postion of the Add New Item button.
window.configure(bg = "#333333")

search_entry = tk.Entry(frame) # This line of code creates the entry box for the Search bar.
search_entry.grid(row=4, column=0, columnspan=2,sticky="ew", padx=20, pady=5)# This line of code sets the size and postion of the search bar. 
search_button = tk.Button(frame, text='Search', command= search, bg='#79AFB8')# This line of code creates the search button and the function search from above is its command.
search_button.grid(row= 4, column =4,padx=20, pady=5, )# This line of code sets the size and postion of the Search button.
reset_button = tk.Button(frame, text="Reset", command= reset_treeview, bg= '#79AFB8')# This line of code creates the Reset button and the reset_treeview  from above is its command.
reset_button.grid(row =9,column=0,columnspan=4, sticky ="news", padx=20, pady=5)# This line of code sets the size and postion of the Reset button.



window.mainloop() # This line of creates a loop around my entire program.