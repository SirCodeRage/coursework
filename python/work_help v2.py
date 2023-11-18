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

# Function to save the order to a file
def save_order():
    order_details = "\n".join(order_items)
    try:
        with open(r"C:\Users\James\Documents\course work\python\order.txt", "w") as file:
            file.write(order_details)
        messagebox.showinfo("Order Saved", "Your order has been saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving the order: {e}")

# Main window
root = tk.Tk()
root.title("Restaurant Ordering System")
root.geometry("1024x768")

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

# Menu categories and items from the images provided
menu = {
    "Small Plates": ["PB+M Cauliflower", "Wings", "Goi Chay", "Pork Belly", "Turmeric Fish", "Jasmine Rice", "Bowl of Noodles"],
    "Special Plates": ["S+P Aubergine", "Pork Belly", "Salt + Pepper Chicken", "Potatoes", "Tofu", "BBQ Courgette", "Cauliflower 3 ways", "Hispi Cabbage", "Sardines", "Soy Glazed Squash", "Tiger wings", "BBQ Mackerel"],
    "Curries": ["Mushroom Curry", "Tofu Curry", "Chicken Curry", "Fish Curry", "Pork Curry", "Veg Curry"],
    "Noodles": ["Bun Pork", "Bun Chicken", "Bun Tofu", "Bun Fish", "Bun Veg"]
}

# Create a grid layout for each menu category and store it in the dictionary
for category, items in menu.items():
    frame = tk.Frame(menu_frame, bg='black')
    menu_frames[category] = frame
    for index, item in enumerate(items):
        # Button color is determined by the item name
        color = "blue"
        if item in ["PB+M Cauliflower", "Goi Chay", "S+P Aubergine", "Potatoes", "Tofu", "BBQ Courgette", "Cauliflower 3 ways", "Hispi Cabbage", "Soy Glazed Squash", "Bun Tofu", "Bun Veg", "Mushroom Curry", "Tofu Curry", "Veg Curry"]:
            color = "green"
        elif item in ["Chicken Curry", "Bun Chicken"]:
            color = "yellow"
        elif item in ["Pork Curry", "Bun Pork", "Pork Belly", "Salt + Pepper Chicken", "Tiger wings", "Wings"]:
            color = "red"
        elif item in ["Jasmine Rice", "Bowl of Noodles"]:
            color = "white"

        btn = tk.Button(frame, text=item, bg=color, fg='black' if color == "white" else 'white',
                        command=lambda item=item: add_to_order(item))
        btn.grid(row=index // 2, column=index % 2, sticky="nsew", padx=5, pady=5)
        frame.grid_columnconfigure(index % 2, weight=1)
        frame.grid_rowconfigure(index // 2, weight=1)

# Menu bar to switch between submenus
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

for category in menu.keys():
    menu_bar.add_command(label=category, command=lambda category=category: show_submenu(category))

# Button to save the order
save_btn = tk.Button(order_frame, text="Save Order", command=save_order, bg='green', fg='white')
save_btn.pack(fill='x')

# Start with a default submenu visible
show_submenu("Small Plates")

# Run the application
root.mainloop()
