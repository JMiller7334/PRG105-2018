import tkinter
import tkinter.messagebox
import pickle
import datetime
from functools import partial


class ServingWindow:
    def __init__(self, food_data, entry_data, key):
        self.root = tkinter.Tk()
        self.root.title(str(key))
        self.root.geometry("350x150")

        # Variables/Data
        self.food_list = food_data
        self.entry_diary = entry_data
        self.current = self.food_list[key]  # Refers to current food entry being used.

        # Frames
        self.label_frame = tkinter.Frame(self.root)
        self.nut_frame = tkinter.Frame(self.root)
        self.serving_frame = tkinter.Frame(self.root)
        self.bottom_frame = tkinter.Frame(self.root)

        # Buttons/Interactive/Labels
        #   Label Frame
        self.label_serving_label = tkinter.Label(self.label_frame, text='Serving size: ')
        self.label_kcal_label = tkinter.Label(self.label_frame, text='Calories per serving: ')
        self.label_carb_label = tkinter.Label(self.label_frame, text='Carbs: ')
        self.label_fat_label = tkinter.Label(self.label_frame, text='Fats: ')
        self.label_protein_label = tkinter.Label(self.label_frame, text='Protein: ')

        #   Top Frame
        self.nut_serving_label = tkinter.Label(self.nut_frame, text=str(self.current[0]))
        self.nut_kcal_label = tkinter.Label(self.nut_frame, text=str(self.current[1]))
        self.nut_carb_label = tkinter.Label(self.nut_frame, text=str(self.current[2]))
        self.nut_fat_label = tkinter.Label(self.nut_frame, text=str(self.current[3]))
        self.nut_protein_label = tkinter.Label(self.nut_frame, text=str(self.current[4]))

        #   Serving Frame
        self.serving_label = tkinter.Label(self.serving_frame, text='Please enter total servings')
        self.serving_entry = tkinter.Entry(self.serving_frame, width=3)

        #   Bottom Frame
        self.back_button = tkinter.Button(self.bottom_frame, text='Go Back', command=self.go_back)
        self.add_button = tkinter.Button(self.bottom_frame, text='Add Entry', command=self.add_entry)

        # Packing
        #   Label Frame
        self.label_serving_label.pack()
        self.label_kcal_label.pack()
        self.label_carb_label.pack()
        self.label_fat_label.pack()
        self.label_protein_label.pack()
        #   Nut Frame
        self.nut_serving_label.pack()
        self.nut_kcal_label.pack()
        self.nut_carb_label.pack()
        self.nut_fat_label.pack()
        self.nut_protein_label.pack()
        #   Serving Frame
        self.serving_label.pack(side='left')
        self.serving_entry.pack(side='left')
        #   Bottom Frame
        self.add_button.pack(side='left')
        self.back_button.pack(side='left')
        #   Frames
        self.label_frame.pack(side='left')
        self.nut_frame.pack(side='right')
        self.serving_frame.pack(side='top')
        self.bottom_frame.pack(side='bottom')

    def add_entry(self):
        print("add!!!")

    def go_back(self):
        print("function: go back")
        save_file(self.food_list, self.entry_diary)
        main_gui = AddEntryWindow(self.food_list, self.entry_diary)
        self.root.destroy()


class AddEntryWindow:
    def __init__(self, food_data, entry_data):
        self.root = tkinter.Tk()
        self.root.title("Entry Management")

        # Variables/Data
        self.food_list = food_data
        self.entry_diary = entry_data

        # Frames
        self.creation_frame = tkinter.Frame(self.root)
        self.existing_frame = tkinter.Frame(self.root)

        # Buttons/interactive/Labels
        #   Creation Frame
        self.new_info_label = tkinter.Label(self.creation_frame, text='Create New Food')
        self.new_name_label = tkinter.Label(self.creation_frame, text='Food name: ')
        self.new_name_entry = tkinter.Entry(self.creation_frame, width=15)
        self.new_serving_label = tkinter.Label(self.creation_frame, text='Serving size information: ')
        self.new_serving_entry = tkinter.Entry(self.creation_frame, width=15)
        self.new_kcal_label = tkinter.Label(self.creation_frame, text='Kcal per serving: ')
        self.new_kcal_entry = tkinter.Entry(self.creation_frame, width=5)
        self.new_carb_label = tkinter.Label(self.creation_frame, text='Carbs per serving: ')
        self.new_carb_entry = tkinter.Entry(self.creation_frame, width=5)
        self.new_fat_label = tkinter.Label(self.creation_frame, text='Fats per serving: ')
        self.new_fat_entry = tkinter.Entry(self.creation_frame, width=5)
        self.new_protein_label = tkinter.Label(self.creation_frame, text='Protein per serving: ')
        self.new_protein_entry = tkinter.Entry(self.creation_frame, width=5)
        self.create_button = tkinter.Button(self.creation_frame, text='Create Food', command=self.create_food)
        self.back_button = tkinter.Button(self.creation_frame, text='Go Back', command=self.go_back)

        #   Existing Frame
        self.existing_info_label = tkinter.Label(self.existing_frame, text='Existing foods will appear here.')
        # ---------------------------------------------------------------------------------------------------------
        # ------------------------------------------- Load Gui Buttons --------------------------------------------
        # ---------------------------------------------------------------------------------------------------------
        self.existing_buttons = {}
        self.existing_commands = {}
        for key in self.food_list:
            imported_info = str(key) + ' | serving size: ' + str(
                self.food_list[key][0]) + ' | calories per serving: ' + str(self.food_list[key][1])

            self.action_with_arg = partial(self.add_food, key)
            self.existing_buttons[key] = tkinter.Button(self.existing_frame, text=str(imported_info),
                                                        command=self.action_with_arg)
            # Packing
            #   Existing Fame
            self.existing_buttons[key].pack(side='bottom')
        # ----------------------------------------------------------------------------------------------------------
        self.existing_info_label.pack()

        #   Creation Frame
        self.new_info_label.pack()
        self.new_name_label.pack()
        self.new_name_entry.pack()
        self.new_serving_label.pack()
        self.new_serving_entry.pack()
        self.new_kcal_label.pack()
        self.new_kcal_entry.pack()
        self.new_carb_label.pack()
        self.new_carb_entry.pack()
        self.new_fat_label.pack()
        self.new_fat_entry.pack()
        self.new_protein_label.pack()
        self.new_protein_entry.pack()
        self.create_button.pack(side='left')
        self.back_button.pack(side='left')

        #   Frames
        self.existing_frame.pack(side='left')
        self.creation_frame.pack(side='left')

    def add_food(self, food):
        print("function: add food to diary")
        serving_GUI = ServingWindow(self.food_list, self.entry_diary, food)
        self.root.destroy()

    def create_food(self):
        print("function: create food")
        name_entry = str(self.new_name_entry.get()).lower()
        serving_entry = str(self.new_serving_entry.get()).lower()
        kcal_entry = float(self.new_kcal_entry.get())
        carb_entry = float(self.new_carb_entry.get())
        fat_entry = float(self.new_fat_entry.get())
        protein_entry = float(self.new_protein_entry.get())
        # ---------------------------------------------------------------------------------------------------------
        # ---------------------------------------------- Write Data -----------------------------------------------
        # ---------------------------------------------------------------------------------------------------------
        search = self.food_list.get(name_entry.lower())
        if search is not None:
            tkinter.messagebox.showinfo("Error", str(name_entry) + " already exists. Please uses a different name")
        else:
            if name_entry == "":
                tkinter.messagebox.showinfo("Error", "You must enter a name for the food entry.")
            else:
                self.food_list.update({name_entry: [serving_entry, kcal_entry, carb_entry, fat_entry, protein_entry]})
                save_file(self.food_list, self.entry_diary)
                new_window = AddEntryWindow(self.food_list, self.entry_diary)
                self.root.destroy()
        # ---------------------------------------------------------------------------------------------------------

    def go_back(self):
        print("function: go back")
        save_file(self.food_list, self.entry_diary)
        main_gui = MainWindow(tkinter.Tk(), self.food_list, self.entry_diary)
        self.root.destroy()


class MainWindow:
    def __init__(self, master, food_data, entry_data):
        self.master = master
        self.master.title("Fitness Tracker")

        # Variables
        self.food_list = food_data
        self.entry_list = entry_data
        self.clock = datetime.datetime.now()

        # Frames
        self.bottom_frame = tkinter.Frame(self.master)
        self.top_frame = tkinter.Frame(self.master)

        # Buttons/Interactive/Labels
        #   Top Frame
        self.prev_button = tkinter.Button(self.top_frame, text='<-', command=self.prev_date)
        self.next_button = tkinter.Button(self.top_frame, text='->', command=self.next_date)
        self.current_date = tkinter.Label(self.top_frame,
                                          text=str(self.clock.month) + '/' + str(self.clock.day) + '/' + str(
                                              self.clock.year))

        #   Bottom Frame
        self.add_button = tkinter.Button(self.bottom_frame, text='Add Food Entry', command=self.add_entry)
        self.exit_button = tkinter.Button(self.bottom_frame, text='Exit Program', command=self.master.destroy)

        # Packing
        #   Buttons
        self.add_button.pack(side='left')
        self.exit_button.pack(side='left')

        self.prev_button.pack(side='left')
        self.current_date.pack(side='left')
        self.next_button.pack(side='left')

        #   Frames
        self.top_frame.pack(side='top')
        self.bottom_frame.pack(side='bottom')

    def add_entry(self):
        print("function: add entry")
        add_entry_GUI = AddEntryWindow(self.food_list, self.entry_list)
        self.master.destroy()

    def prev_date(self):
        print("function: prev date")

    def next_date(self):
        print("function: next date")


def save_file(food_data, entry_data):
    output_file_food = open('food_data.dat', 'wb')
    pickle.dump(food_data, output_file_food)
    print(food_data)

    output_file_entries = open('entries_data.dat', 'wb')
    pickle.dump(entry_data, output_file_entries)
    print(entry_data)


def main():
    try:
        input_file_food = open("food_data.dat", 'rb')
        data_file_food = pickle.load(input_file_food)

        input_file_entries = open("entries_data.dat", 'rb')
        data_file_entries = pickle.load(input_file_entries)
    except(FileNotFoundError, IOError):
        data_file_food = {}
        data_file_entries = {}

    root = tkinter.Tk()
    main_gui = MainWindow(root, data_file_food, data_file_entries)
    root.mainloop()


main()
