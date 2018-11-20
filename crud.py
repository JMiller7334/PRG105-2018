"""
    Create a CRUD application with a GUI interface
"""

import pickle
import tkinter
import tkinter.messagebox


class CrudGUI:
    def __init__(self, master, cust):
        self.master = master
        self.master.title('Welcome Menu')
        self.customer_list = cust
        self.radio_var = 0

        self.top_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # create radio buttons
        self.look = tkinter.Radiobutton(self.top_frame, text="Look up customer", variable=self.radio_var, value=1)
        self.add = tkinter.Radiobutton(self.top_frame, text="Add a customer", variable=self.radio_var, value=2)
        self.change = tkinter.Radiobutton(self.top_frame, text="Change customer information", variable=self.radio_var,
                                          value=3)
        self.delete = tkinter.Radiobutton(self.top_frame, text="Delete a customer", variable=self.radio_var, value=4)

        # pack radio buttons
        self.look.pack(anchor='w', padx=20)
        self.add.pack(anchor='w', padx=20)
        self.change.pack(anchor='w', padx=20)
        self.delete.pack(anchor='w', padx=20)

        # create ok and quit buttons
        self.ok_button = tkinter.Button(self.bottom_frame, text="OK", command=self.open_menu)
        self.quit_button = tkinter.Button(self.bottom_frame, text="QUIT", command=self.master.destroy)

        # pack buttons
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        print(self.customer_list)

    def open_menu(self):
        if self.radio_var.get() == 1:
            look_up = LookGUI(self.customer_list)
        elif self.radio_var.get() == 2:
            add_user = AddGUI(self.customer_list)
        elif self.radio_var.get() == 3:
            edit_user = EditGUI(self.customer_list)
        else:
            delete_user = DeleteGUI(self.customer_list)


class LookGUI:
    def __init__(self, customer_data):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # widgets for top frame
        self.search_label = tkinter.Label(self.top_frame, text='Enter customer email to look for: ')
        self.search_entry = tkinter.Entry(self.top_frame, width=15)

        # pack top frame
        self.search_label.pack(side='left')
        self.search_entry.pack(side='left')

        # buttons for bottom frame
        self.search_button = tkinter.Button(self.bottom_frame, text='Search', command=self.search)
        self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.main_window.destroy)

        # pack bottom frame
        self.search_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Email Data
        self.data = customer_data

    def search(self):
        user_email = str(self.search_entry.get()).lower()
        search = self.data.get(user_email.lower())
        if search is None:
            tkinter.messagebox.showinfo("No Info Found", str(user_email) + " is not a valid entry within the database.")
            self.main_window.destroy()
        else:
            tkinter.messagebox.showinfo("Entry Found", "Email Address: " + user_email + " | Email Owner: " + search)
            self.main_window.destroy()


class AddGUI:
    def __init__(self, customer_data):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # widgets for top frame
        self.email_label = tkinter.Label(self.top_frame, text='Enter customer email to add: ')
        self.email_entry = tkinter.Entry(self.top_frame, width=30)
        self.name_label = tkinter.Label(self.middle_frame, text='Enter customer name to add: ')
        self.name_entry = tkinter.Entry(self.middle_frame, width=30)

        # pack top frame
        self.email_label.pack(side='left')
        self.email_entry.pack(side='left')
        self.name_label.pack(side='left')
        self.name_entry.pack(side='left')

        # buttons for bottom frame
        self.add_button = tkinter.Button(self.bottom_frame, text='Add email', command=self.add_email)
        self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.main_window.destroy)

        # pack bottom frame
        self.add_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        # Email Data
        self.data = customer_data

    def add_email(self):
        user_email = str(self.email_entry.get()).lower()
        user_name = str(self.name_entry.get()).lower()
        search = self.data.get(user_email.lower())

        if search is not None:
            tkinter.messagebox.showinfo("Info", str(user_email) + " already exists within the database.")
            self.main_window.destroy()
        else:
            if user_email == "":
                tkinter.messagebox.showinfo("Error", "You must enter an email to add.")
                self.main_window.destroy()
            else:
                self.data.update({user_email.lower(): user_name.lower()})
                tkinter.messagebox.showinfo("Database updated", str(user_email) + " has been added as the email and "
                                            + user_name + " has been added as the email's owner")
                save_file(self.data)
                self.main_window.destroy()


class EditGUI:
    def __init__(self, customer_data):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.middle_frame2 = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # widgets for top frame
        self.email_label = tkinter.Label(self.top_frame, text='Enter customer email to edit: ')
        self.email_entry = tkinter.Entry(self.top_frame, width=30)

        self.new_label = tkinter.Label(self.middle_frame2, text='Enter new customer email: ')
        self.new_entry = tkinter.Entry(self.middle_frame2, width=30)

        self.name_label = tkinter.Label(self.middle_frame, text='Enter new customer name: ')
        self.name_entry = tkinter.Entry(self.middle_frame, width=30)

        # pack top frame
        self.email_label.pack(side='left')
        self.email_entry.pack(side='left')
        self.name_label.pack(side='left')
        self.name_entry.pack(side='left')
        self.new_label.pack(side='left')
        self.new_entry.pack(side='left')

        # buttons for bottom frame
        self.edit_button = tkinter.Button(self.bottom_frame, text='Edit email', command=self.edit_email)
        self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.main_window.destroy)

        # pack bottom frame
        self.edit_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame2.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        # Email Data
        self.data = customer_data

    def edit_email(self):
        user_email = str(self.email_entry.get()).lower()
        new_email = str(self.new_entry.get()).lower()
        new_name = str(self.name_entry.get()).lower()
        search = self.data.get(user_email.lower())

        if search is None:
            tkinter.messagebox.showinfo("No Entry Found", str(user_email) + " does not exists within the database.")
            self.main_window.destroy()
        else:
            self.data[new_email] = self.data[user_email]
            self.data.pop(user_email)
            user_email = new_email
            self.data[user_email] = new_name

            save_file(self.data)
            self.main_window.destroy()


class DeleteGUI:
    def __init__(self, customer_data):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # widgets for top frame
        self.email_label = tkinter.Label(self.top_frame, text='Enter customer email to delete: ')
        self.email_entry = tkinter.Entry(self.top_frame, width=30)

        # pack top frame
        self.email_label.pack(side='left')
        self.email_entry.pack(side='left')

        # buttons for bottom frame
        self.add_button = tkinter.Button(self.bottom_frame, text='Delete email', command=self.delete_email)
        self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.main_window.destroy)

        # pack bottom frame
        self.add_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        # Email Data
        self.data = customer_data
        print(self.data)

    def delete_email(self):
        user_email = str(self.email_entry.get()).lower()
        search = self.data.get(user_email.lower())

        if search is None:
            tkinter.messagebox.showinfo("No Entry Found", user_email + " is not a valid entry within the database.")
            self.main_window.destroy()
        else:
            tkinter.messagebox.showinfo("Entry Deleted", "Data for this entry has been deleted.")
            self.data.pop(user_email)
            save_file(self.data)
            self.main_window.destroy()


def save_file(data):
    output_file = open('customer_file.dat', 'wb')
    pickle.dump(data, output_file)
    print(data)


def main():
    try:
        input_file = open("customer_file.dat", 'rb')
        customers = pickle.load(input_file)
    except(FileNotFoundError, IOError):
        customers = {}

    root = tkinter.Tk()
    menu_gui = CrudGUI(root, customers)
    root.mainloop()


main()
