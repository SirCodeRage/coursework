import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
import os

# Function to add an item to the order
def add_to_order(item_name):
    order_items.append(item_name)
    update_order_listbox()

# Function to update the Listbox with order items
def update_order_listbox():
    order_listbox.delete(0, tk.END)
    for item in order_items:
        order_listbox.insert(tk.END, item)

# Function to remove the selected item from the order
def remove_selected_item():
    selected_indices = order_listbox.curselection()
    for index in selected_indices[::-1]:
        del order_items[index]
    update_order_listbox()

# Function to clear the entire order
def clear_order():
    order_items.clear()
    update_order_listbox()

# Function to save the order to a file
def save_order():
    order_details = "\n".join(order_items)
    order_file = get_next_order_filename()
    try:
        with open(order_file, "w") as file:
            file.write(order_details)
        messagebox.showinfo("Order Saved", f"Your order has been saved successfully in {order_file}")
        clear_order()  # Clear the order list after saving
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving the order: {e}")

# Function to get the next order file name
def get_next_order_filename():
    order_number = 1
    while os.path.exists(f"C:\\Users\\James\\Documents\\course work\\python\\order_{order_number}.txt"):
        order_number += 1
    return f"C:\\Users\\James\\Documents\\course work\\python\\order_{order_number}.txt"

# Main window
root = tk.Tk()
root.title("Restaurant Ordering System")
root.geometry("1024x768")

# Define font for buttons
button_font = tkFont.Font(family="Helvetica", size=14)

# List to keep track of order items
order_items = []

# Order display on the left
order_frame = tk.Frame(root, bg='white', bd=2)
order_frame.pack(side="left", fill="y", expand=False)

# Listbox to display the order
order_listbox = tk.Listbox(order_frame, bg='white', fg='black')
order_listbox.pack(fill="both", expand=True)

# Menu frame on the right
menu_frame = tk.Frame(root, bg='black')
menu_frame.pack(side="left", fill="both", expand=True)

# Dictionary to keep track of category frames
menu_frames = {}

# Menu categories and items
menu = {
  
    "Small Plates": ["PB+M Cauliflower", "Wings", "Goi Chay", "Pork Belly", "Turmeric Fish", "Jasmine Rice", "Bowl of Noodles"],
    "Special Plates": ["S+P Aubergine", "Pork Belly", "Salt + Pepper Chicken", "Potatoes", "Tofu", "BBQ Courgette", "Cauliflower 3 ways", "Hispi Cabbage", "Sardines", "Soy Glazed Squash", "Tiger wings", "BBQ Mackerel"],
    "Curries": ["Mushroom Curry", "Tofu Curry", "Chicken Curry", "Fish Curry", "Pork Curry", "Veg Curry"],
    "Noodles": ["Bun Pork", "Bun Chicken", "Bun Tofu", "Bun Fish", "Bun Veg"]
}


# Assign colors to specific items
item_colors = {
    # Green items
    "PB+M Cauliflower": "green", "Goi Chay": "green", "S+P Aubergine": "green",
    "Potatoes": "green", "Tofu": "green", "BBQ Courgette": "green",
    "Cauliflower 3 ways": "green", "Hispi Cabbage": "green", "Soy Glazed Squash": "green",
    "Bun Tofu": "green", "Bun Veg": "green", "Mushroom Curry": "green",
    "Tofu Curry": "green", "Veg Curry": "green",
    # Lighter Yellow items
    "Chicken Curry": "orange", "Bun Chicken": "orange",
    # Red items
    "Pork Curry": "red", "Bun Pork": "red", "Pork Belly": "red",
    "Salt + Pepper Chicken": "red", "Tiger wings": "red", "Wings": "red",
    # White items
    "Jasmine Rice": "white", "Bowl of Noodles": "white",
    # Default color
    "default": "blue"
}

# Function to get the color for an item
def get_item_color(item):
    return item_colors.get(item, item_colors["default"])

# Function to show a particular submenu
def show_submenu(category):
    # Hide all frames
    for frame in menu_frames.values():
        frame.pack_forget()
    # Show the selected frame
    menu_frames[category].pack(expand=True, fill="both")

# Create a grid layout for each menu category and store it in the dictionary
for category, items in menu.items():
    frame = tk.Frame(menu_frame, bg='black')
    menu_frames[category] = frame
    for index, item in enumerate(items):
        btn = tk.Button(frame, text=item, bg=get_item_color(item), fg='black' if get_item_color(item) == 'white' else 'white',
                        font=button_font, command=lambda item=item: add_to_order(item))
        btn.grid(row=index // 2, column=index % 2, sticky="nsew", padx=5, pady=5)
        frame.grid_columnconfigure(index % 2, weight=1)
        frame.grid_rowconfigure(index // 2, weight=1)

# Menu bar to switch between submenus
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

for category in menu.keys():
    menu_bar.add_command(label=category, command=lambda category=category: show_submenu(category))

# Button to remove selected item from the order
remove_item_btn = tk.Button(order_frame, text="Remove Selected Item", command=remove_selected_item, bg='orange', fg='white')
remove_item_btn.pack(fill='x')

# Button to clear the order
clear_order_btn = tk.Button(order_frame, text="Clear Order", command=clear_order, bg='red', fg='white')
clear_order_btn.pack(fill='x')

# Button to save the order
save_btn = tk.Button(order_frame, text="Save Order", command=save_order, bg='green', fg='white')
save_btn.pack(fill='x')

# Start with a default submenu visible
show_submenu(next(iter(menu)))

# Run the application
root.mainloop()
