from tkinter import *
import csv
import os

def save_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    
    with open('contacts.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, phone])
    
    name_entry.delete(0, END)
    phone_entry.delete(0, END)


window = Tk()
window.title("Contact Book")
window.geometry("600x400")


Label(window, text="Name").grid(row=0, column=0, padx=10, pady=10)
name_entry = Entry(window)
name_entry.grid(row=0, column=1, padx=10, pady=10)

Label(window, text="Phone").grid(row=1, column=0, padx=10, pady=10)
phone_entry = Entry(window)
phone_entry.grid(row=1, column=1, padx=10, pady=10)


save_button = Button(window, text="Save Contact", command=save_contact)
save_button.grid(row=3, column=0, columnspan=2, pady=20)

window.mainloop()