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

# Function to show a particular submenu
def show_submenu(category):
    # Hide all frames
    for frame in menu_frames.values():
        frame.pack_forget()
    # Show the selected frame
    menu_frames[category].pack(expand=True, fill="both")
    # Update the submenu label to indicate the current category
    submenu_label.config(text=submenu_labels[category])

# Main window setup
root = tk.Tk()
root.title("Restaurant Ordering System")
root.geometry("1024x768")
# Define font for buttons
button_font = tkFont.Font(family="Helvetica", size=16, weight="bold")
# List to keep track of order items
order_items = []

# Menu frame on the top
menu_frame = tk.Frame(root)
menu_frame.pack(side="top", fill="x", expand=False)

# Define submenu labels
submenu_labels = {
    "Small Plates": "Small Plates",
    "Special Plates": "Special Plates",
    "Curries": "Curries",
    "Noodles": "Noodles"
}

# Create buttons for each category to display its submenu within the menu frame
for category in submenu_labels.keys():
    btn = tk.Button(menu_frame, text=category, font=button_font,
                    command=lambda cat=category: show_submenu(cat))
    btn.pack(side="left", padx=5, pady=5)

# Create a label widget to display the current submenu category
submenu_label = tk.Label(menu_frame, text="", font=button_font)
submenu_label.pack(side="top")

# Order display on the left
order_frame = tk.Frame(root, bg='white', bd=2)
order_frame.pack(side="left", fill="y", expand=False)

# Listbox to display the order
order_listbox = tk.Listbox(order_frame, bg='white', fg='black', font=button_font)
order_listbox.pack(fill="both", expand=True)

# Dictionary to keep track of category frames
menu_frames = {category: tk.Frame(root) for category in submenu_labels}

# Create a grid layout for each menu category and store it in the dictionary
submenu_items = {
    "Small Plates": ["PB+M Cauliflower", "Wings", "Goi Chay", "Pork Belly", "Turmeric Fish", "Jasmine Rice", "Bowl of Noodles"],
    "Special Plates": ["S+P Aubergine", "Pork Belly", "Salt + Pepper Chicken", "Potatoes", "Tofu", "BBQ Courgette", "Cauliflower 3 ways", "Hispi Cabbage", "Sardines", "Soy Glazed Squash", "Tiger wings", "BBQ Mackerel"],
    "Curries": ["Mushroom Curry", "Tofu Curry", "Chicken Curry", "Fish Curry", "Pork Curry", "Veg Curry"],
    "Noodles": ["Bun Pork", "Bun Chicken", "Bun Tofu", "Bun Fish", "Bun Veg"]
}

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
    "Fish Curry": "blue", "Turmeric Fish": "blue", "Bun Fish": "blue", "BBQ Mackerel": "blue",
    "Sardines": "blue"
}

# Function to get the color for an item
def get_item_color(item):
    return item_colors.get(item, "grey")  # Fallback color

for category, items in submenu_items.items():
    frame = menu_frames[category]
    for index, item in enumerate(items):
        color = get_item_color(item)
        btn = tk.Button(frame, text=item, bg=color, fg='black' if get_item_color(item) == 'white' else 'white',
                        font=button_font, command=lambda item=item: add_to_order(item))
        btn.grid(row=index // 2, column=index % 2, sticky="nsew", padx=5, pady=5)
        frame.grid_columnconfigure(index % 2, weight=1)
        frame.grid_rowconfigure(index // 2, weight=1)

# Button to remove selected item from the order
remove_item_btn = tk.Button(order_frame, text="Remove Selected Item", command=remove_selected_item, bg='orange', fg='white', font=button_font)
remove_item_btn.pack(fill='x')

# Button to clear the order
clear_order_btn = tk.Button(order_frame, text="Clear Order", command=clear_order, bg='red', fg='white', font=button_font)
clear_order_btn.pack(fill='x')

# Button to save the order
save_btn = tk.Button(order_frame, text="Save Order", command=save_order, bg='green', fg='white', font=button_font)
save_btn.pack(fill='x')

# Start with the first submenu visible
first_category = next(iter(submenu_labels))
show_submenu(first_category)

# Run the application
root.mainloop()
