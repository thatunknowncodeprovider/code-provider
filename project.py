import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# Database connection
db = mysql.connector.connect(host="localhost",user="root",password="admin@1234",database="pharmacy_management")
cursor = db.cursor()

# Functions
def add_medicine():
    name = name_entry.get()
    quantity = quantity_entry.get()
    price = price_entry.get()
    expiry_date = expiry_entry.get()
    
    if not (name and quantity and price and expiry_date):
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        query = "INSERT INTO medicines (name, quantity, price, expiry_date) VALUES (%s, %s, %s, %s)"
        values = (name, int(quantity), float(price), expiry_date)
        cursor.execute(query, values)
        db.commit()
        messagebox.showinfo("Success", "Medicine added successfully!")
        clear_entries()
        view_medicines()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def view_medicines():
    for item in tree.get_children():
        tree.delete(item)
    
    query = "SELECT * FROM medicines"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row)

def update_medicine():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror("Error", "Select a medicine to update!")
        return
    
    item = tree.item(selected_item)
    medicine_id = item['values'][0]
    
    name = name_entry.get()
    quantity = quantity_entry.get()
    price = price_entry.get()
    expiry_date = expiry_entry.get()
    
    if not (name and quantity and price and expiry_date):
        messagebox.showerror("Error", "All fields are required!")
        return
    
    try:
        query = "UPDATE medicines SET name = %s, quantity = %s, price = %s, expiry_date = %s WHERE id = %s"
        values = (name, int(quantity), float(price), expiry_date, medicine_id)
        cursor.execute(query, values)
        db.commit()
        messagebox.showinfo("Success", "Medicine updated successfully!")
        clear_entries()
        view_medicines()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_medicine():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror("Error", "Select a medicine to delete!")
        return
    
    item = tree.item(selected_item)
    medicine_id = item['values'][0]
    
    try:
        query = "DELETE FROM medicines WHERE id = %s"
        cursor.execute(query, (medicine_id,))
        db.commit()
        messagebox.showinfo("Success", "Medicine deleted successfully!")
        view_medicines()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def clear_entries():
    name_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    expiry_entry.delete(0, tk.END)

# GUI
root = tk.Tk()
root.title("Pharmacy Management System")
root.geometry("800x600")

# Labels and Entry Fields
tk.Label(root, text="Medicine Name:").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Quantity:").grid(row=1, column=0, padx=10, pady=10)
quantity_entry = tk.Entry(root)
quantity_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Price:").grid(row=2, column=0, padx=10, pady=10)
price_entry = tk.Entry(root)
price_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Expiry Date (YYYY-MM-DD):").grid(row=3, column=0, padx=10, pady=10)
expiry_entry = tk.Entry(root)
expiry_entry.grid(row=3, column=1, padx=10, pady=10)

# Buttons
tk.Button(root, text="Add Medicine", command=add_medicine).grid(row=4, column=0, padx=10, pady=10)
tk.Button(root, text="Update Medicine", command=update_medicine).grid(row=4, column=1, padx=10, pady=10)
tk.Button(root, text="Delete Medicine", command=delete_medicine).grid(row=5, column=0, padx=10, pady=10)
tk.Button(root, text="Clear Fields", command=clear_entries).grid(row=5, column=1, padx=10, pady=10)

# Treeview for Medicines
tree = ttk.Treeview(root, columns=("ID", "Name", "Quantity", "Price", "Expiry Date"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Quantity", text="Quantity")
tree.heading("Price", text="Price")
tree.heading("Expiry Date", text="Expiry Date")
tree.column("ID", width=50)
tree.column("Name", width=150)
tree.column("Quantity", width=100)
tree.column("Price", width=100)
tree.column("Expiry Date", width=100)
tree.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Load data initially
view_medicines()

# Run the application
root.mainloop()
