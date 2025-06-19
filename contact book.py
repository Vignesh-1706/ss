import tkinter as tk
from tkinter import messagebox, simpledialog

# Contact list: stores dictionaries of contact info
contacts = []

# Add Contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts.append({
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        })
        messagebox.showinfo("Success", f"Contact '{name}' added!")
        clear_entries()
        show_contacts()
    else:
        messagebox.showwarning("Missing Info", "Name and Phone are required.")

# View all contacts
def show_contacts():
    contact_list.delete(0, tk.END)
    for i, c in enumerate(contacts):
        contact_list.insert(tk.END, f"{i+1}. {c['name']} - {c['phone']}")

# Search contact
def search_contact():
    query = search_entry.get().lower()
    contact_list.delete(0, tk.END)
    for i, c in enumerate(contacts):
        if query in c["name"].lower() or query in c["phone"]:
            contact_list.insert(tk.END, f"{i+1}. {c['name']} - {c['phone']}")
    if contact_list.size() == 0:
        contact_list.insert(tk.END, "No contact found.")

# Show selected contact's full details
def show_details(event):
    try:
        index = contact_list.curselection()[0]
        real_index = int(contact_list.get(index).split(".")[0]) - 1
        contact = contacts[real_index]
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
        name_entry.insert(0, contact["name"])
        phone_entry.insert(0, contact["phone"])
        email_entry.insert(0, contact["email"])
        address_entry.insert(0, contact["address"])
    except:
        pass

# Update contact
def update_contact():
    try:
        index = contact_list.curselection()[0]
        real_index = int(contact_list.get(index).split(".")[0]) - 1
        contacts[real_index]["name"] = name_entry.get()
        contacts[real_index]["phone"] = phone_entry.get()
        contacts[real_index]["email"] = email_entry.get()
        contacts[real_index]["address"] = address_entry.get()
        messagebox.showinfo("Success", "Contact updated.")
        show_contacts()
        clear_entries()
    except:
        messagebox.showwarning("Error", "Select a contact to update.")

# Delete contact
def delete_contact():
    try:
        index = contact_list.curselection()[0]
        real_index = int(contact_list.get(index).split(".")[0]) - 1
        deleted_name = contacts[real_index]["name"]
        del contacts[real_index]
        messagebox.showinfo("Deleted", f"Contact '{deleted_name}' deleted.")
        show_contacts()
        clear_entries()
    except:
        messagebox.showwarning("Error", "Select a contact to delete.")

# Clear all entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Contact Book")
root.geometry("600x500")

# Labels & Entry Fields
tk.Label(root, text="Name:").place(x=20, y=20)
name_entry = tk.Entry(root, width=30)
name_entry.place(x=120, y=20)

tk.Label(root, text="Phone:").place(x=20, y=60)
phone_entry = tk.Entry(root, width=30)
phone_entry.place(x=120, y=60)

tk.Label(root, text="Email:").place(x=20, y=100)
email_entry = tk.Entry(root, width=30)
email_entry.place(x=120, y=100)

tk.Label(root, text="Address:").place(x=20, y=140)
address_entry = tk.Entry(root, width=30)
address_entry.place(x=120, y=140)

# Buttons
tk.Button(root, text="Add Contact", width=15, command=add_contact).place(x=400, y=20)
tk.Button(root, text="Update Contact", width=15, command=update_contact).place(x=400, y=60)
tk.Button(root, text="Delete Contact", width=15, command=delete_contact).place(x=400, y=100)

# Search
tk.Label(root, text="Search:").place(x=20, y=190)
search_entry = tk.Entry(root, width=25)
search_entry.place(x=80, y=190)
tk.Button(root, text="Search", command=search_contact).place(x=280, y=185)

# Contact List
tk.Label(root, text="Contact List:").place(x=20, y=230)
contact_list = tk.Listbox(root, width=60, height=12)
contact_list.place(x=20, y=260)
contact_list.bind("<<ListboxSelect>>", show_details)

# Run App
root.mainloop()
