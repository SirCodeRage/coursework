import tkinter as tk
from tkinter import messagebox

# Function to add an item to the order
def add_to_order(item_name):
    order_items.append(item_name)
    update_order_listbox()

# Function to update the Listbox with order items
def update_order_listbox():
    order_listbox.delete(0, tk.END)
    for item in order_items:
        order_listbox.insert(tk.END, item)

# Function to show a particular submenu
def show_submenu(category):
    # Hide all frames
    for frame in menu_frames.values():
        frame.pack_forget()
    # Show the selected frame
    menu_frames[category].pack(expand=True, fill="both")

# Function to save the order to a file and show a confirmation message
def save_order():
    with open("order.txt", "w") as file:
        for item in order_items:
            file.write(f"{item}\n")
    messagebox.showinfo("Order Saved", "Your order has been saved successfully!")

# Main window
root = tk.Tk()
root.title("Restaurant Ordering System")
root.geometry("1024x768")

# Menu categories and items
menu = {
    "Small Plates": ["PB+M Cauliflower", "Wings", "Goi Chay", "Pork Belly", "Turmeric Fish", "Jasmine Rice"],
    "Special Plates": ["S+P Aubergine", "Salt + Pepper Chicken", "Tofu", "BBQ Courgette", "Cauliflower 3 ways", "Hispi Cabbage"],
    "Curries": ["Mushroom Curry", "Tofu Curry", "Chicken Curry", "Fish Curry", "Pork Curry", "Veg Curry"],
    "Noodles": ["Bun Pork", "Bun Chicken", "Bun Tofu", "Bun Fish", "Bun Veg"]
}

# List to keep track of order items
order_items = []

# Order display on the left
order_frame = tk.Frame(root)
order_frame.pack(side="left", fill="both", expand=False)

# Listbox to display the order
order_listbox = tk.Listbox(order_frame)
order_listbox.pack(fill="both", expand=True)

# Menu frame on the right
menu_frame = tk.Frame(root)
menu_frame.pack(side="right", fill="both", expand=True)

# Dictionary to keep track of category frames
menu_frames = {}

# Create a frame for each menu category and store it in the dictionary
for category, items in menu.items():
    frame = tk.Frame(menu_frame)
    menu_frames[category] = frame
    for item in items:
        btn = tk.Button(frame, text=item, command=lambda item=item: add_to_order(item))
        btn.pack(side="top", fill="x")

# Menu bar to switch between submenus
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

for category in menu.keys():
    menu_bar.add_command(label=category, command=lambda category=category: show_submenu(category))

# Button to save the order
save_btn = tk.Button(order_frame, text="Save Order", command=save_order)
save_btn.pack()

# Run the application
root.mainloop()
