from tkinter import *
import csv


def save_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    
    #creates a csv file and writes the name and phone number to it
    with open('contacts.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, phone])
    
    name_entry.delete(0, END)
    phone_entry.delete(0, END)
    
    load_contacts()


def load_contacts():
    contact_listbox.delete(0, END)
    try:
        with open('contacts.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                contact_listbox.insert(END, f"{row[0]}, {row[1]}")
    except FileNotFoundError:
        contact_listbox.insert(END, "Contact not found.")


def select_contact(event):
    try:
        selected_contact = contact_listbox.get(contact_listbox.curselection())
        name, phone = selected_contact.split(", ")
        name_entry.delete(0, END)
        name_entry.insert(0, name)
        phone_entry.delete(0, END)
        phone_entry.insert(0, phone)
    except IndexError:
        pass


def update_contact():
    selected_index = contact_listbox.curselection()
    if not selected_index:
        return
    
    name = name_entry.get()
    phone = phone_entry.get()
    
    contacts = []
    with open('contacts.csv', mode='r') as file:
        reader = csv.reader(file)
        contacts = list(reader)
    
    contacts[selected_index[0]] = [name, phone]
    
    with open('contacts.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contacts)
    
    name_entry.delete(0, END)
    phone_entry.delete(0, END)
    
    load_contacts()


window = Tk()
window.title("Contact Book")
window.geometry("600x400")

#Creates the Name and Phone labels and entry boxes
Label(window, text="Name").grid(row=0, column=0, padx=10, pady=10)
name_entry = Entry(window)
name_entry.grid(row=0, column=1, padx=10, pady=10)

Label(window, text="Phone").grid(row=1, column=0, padx=10, pady=10)
phone_entry = Entry(window)
phone_entry.grid(row=1, column=1, padx=10, pady=10)

#adds the contact list
contact_listbox = Listbox(window, width=50)
contact_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
contact_listbox.bind('<<ListboxSelect>>', select_contact)

#adds the save button
save_button = Button(window, text="Save Contact", command=save_contact)
save_button.grid(row=3, column=0, columnspan=2, pady=10)

#adds the update button
update_button = Button(window, text="Update Contact", command=update_contact)
update_button.grid(row=4, column=0, columnspan=2, pady=10)

load_contacts()

window.mainloop()