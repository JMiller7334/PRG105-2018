import tkinter
import tkinter.messagebox
import pickle
import datetime
from functools import partial


# ------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------- Serving Window ----------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
class ServingWindow:
    def __init__(self, food_data, entry_data, key, current_date):
        self.root = tkinter.Tk()
        self.root.title(str(key))
        self.root.geometry("400x150")

        # Variables/Data
        self.food_list = food_data
        self.entry_diary = entry_data

        self.current_diary = current_date
        self.current = self.food_list[key]
        self.key = key  # Refers to current food entry being used.

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
        self.delete_button = tkinter.Button(self.bottom_frame, text='Delete This Food', command=self.delete_food)

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
        self.delete_button.pack(side='right')
        #   Frames
        self.label_frame.pack(side='left')
        self.nut_frame.pack(side='right')
        self.serving_frame.pack(side='top')
        self.bottom_frame.pack(side='bottom')

    def add_entry(self):
        print("function: add food entry")
        user_entry = str(self.serving_entry.get())
        try:
            user_entry = float(user_entry)
            self.write_entry(user_entry)
        except ValueError:
            tkinter.messagebox.showinfo("Error", "You must enter a number.")

    def write_entry(self, servings):
        # ---------------------------------------------- Write Data -----------------------------------------------
        self.entry_diary[self.current_diary].append([self.key, servings])
        save_file(self.food_list, self.entry_diary)
        new_window = AddEntryWindow(self.food_list, self.entry_diary, self.current_diary)
        self.root.destroy()
        # ----------------------------------------------------------------------------------------------------------

    def go_back(self):
        print("function: go back")
        save_file(self.food_list, self.entry_diary)
        entry_gui = AddEntryWindow(self.food_list, self.entry_diary, self.current_diary)
        self.root.destroy()

    def delete_food(self):
        print("deleting food entry")
        self.food_list.pop(self.key)
        save_file(self.food_list, self.entry_diary)
        entry_gui = AddEntryWindow(self.food_list, self.entry_diary, self.current_diary)
        self.root.destroy()


# ------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------- Add Entry Window --------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
class AddEntryWindow:
    def __init__(self, food_data, entry_data, current_date):
        self.root = tkinter.Tk()
        self.root.title("Entry Management")

        # Variables/Data
        self.food_list = food_data
        self.entry_diary = entry_data
        self.current_diary = current_date

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
        self.search_entry = tkinter.Entry(self.existing_frame, width=15)
        self.search_label = tkinter.Label(self.existing_frame, text='Look up by food name: ')
        self.search_button = tkinter.Button(self.existing_frame, text='Search', command=self.search_food)

        self.existing_info_label = tkinter.Label(self.existing_frame, text='Existing foods will below here.')
        # ------------------------------------------- Load Gui Buttons --------------------------------------------
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
        self.search_label.pack()
        self.search_entry.pack()
        self.search_button.pack()
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
        serving_GUI = ServingWindow(self.food_list, self.entry_diary, food, self.current_diary)
        self.root.destroy()

    def search_food(self):
        print("function: search food")
        user_search = str(self.search_entry.get()).lower()
        search = self.food_list.get(user_search)
        if search is not None:
            self.add_food(user_search)

    def create_food(self):
        print("function: create food")
        name_entry = str(self.new_name_entry.get()).lower()
        serving_entry = str(self.new_serving_entry.get()).lower()
        kcal_entry = str(self.new_kcal_entry.get())
        carb_entry = str(self.new_carb_entry.get())
        fat_entry = str(self.new_fat_entry.get())
        protein_entry = str(self.new_protein_entry.get())
        # ---------------------------------------------- Write Data -----------------------------------------------
        search = self.food_list.get(name_entry.lower())
        if search is not None:
            tkinter.messagebox.showinfo("Error", str(name_entry) + " already exists. Please uses a different name")
        else:
            # ---- Validate and Check User Entries ----
            if name_entry == "":
                tkinter.messagebox.showinfo("Error", "You must enter a name for the food entry.")
            elif serving_entry == "":
                tkinter.messagebox.showinfo("Error", "You must enter a serving size description for the food entry.")
            else:
                # Calories
                if kcal_entry == "":
                    kcal_entry = float(0.0)
                elif kcal_entry.isdigit():
                    kcal_entry = float(kcal_entry)
                else:
                    kcal_entry = float(0.0)
                # Carbs
                if carb_entry == "":
                    carb_entry = float(0.0)
                elif carb_entry.isdigit():
                    carb_entry = float(carb_entry)
                else:
                    carb_entry = float(0.0)
                # Fats
                if fat_entry == "":
                    fat_entry = float(0.0)
                elif fat_entry.isdigit():
                    fat_entry = float(fat_entry)
                else:
                    fat_entry = float(0.0)
                # Protein
                if protein_entry == "":
                    protein_entry = float(0.0)
                elif protein_entry.isdigit():
                    protein_entry = float(protein_entry)
                else:
                    protein_entry = float(0.0)

                # --------- Data Writing ---------
                self.food_list.update({name_entry: [serving_entry, kcal_entry, carb_entry, fat_entry, protein_entry]})
                save_file(self.food_list, self.entry_diary)
                new_window = AddEntryWindow(self.food_list, self.entry_diary, self.current_diary)
                self.root.destroy()
        # ---------------------------------------------------------------------------------------------------------

    def go_back(self):
        print("function: go back")
        save_file(self.food_list, self.entry_diary)
        main_gui = MainWindow(tkinter.Tk(), self.food_list, self.entry_diary, self.current_diary)
        self.root.destroy()


# ------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------- Main Window -------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
class MainWindow:
    def __init__(self, master, food_data, entry_data, current):
        self.master = master
        self.master.title("Fitness Tracker")
        self.master.geometry("450x600")

        # Variables
        self.food_list = food_data
        self.entry_diary = entry_data
        self.current_diary = current

        # Frames
        self.bottom_frame = tkinter.Frame(self.master)
        self.top_frame = tkinter.Frame(self.master)
        self.existing_frame = tkinter.Frame(self.master)

        # Buttons/Interactive/Labels
        #   Top Frame
        self.prev_button = tkinter.Button(self.top_frame, text='<-', command=self.prev_date)
        self.next_button = tkinter.Button(self.top_frame, text='->', command=self.next_date)
        self.current_date = tkinter.Label(self.top_frame, text=str(self.current_diary))

        #   Bottom Frame
        self.add_button = tkinter.Button(self.bottom_frame, text='Add Food Entry', command=self.add_entry)
        self.exit_button = tkinter.Button(self.bottom_frame, text='Exit Program', command=self.master.destroy)

        # ------------------------------------------- Load Gui Buttons --------------------------------------------
        self.existing_buttons = {}
        self.existing_commands = {}
        key_send = 0
        for listing in self.entry_diary[self.current_diary]:
            imported_info = str("Food Name: " + str(listing[0]))
            print(listing[0])

            self.action_with_arg = partial(self.manage_entry, listing[0], key_send)
            self.existing_buttons[listing[0]] = tkinter.Button(self.existing_frame, text=str(imported_info),
                                                               command=self.action_with_arg)
            # Packing
            #   Existing Fame
            self.existing_buttons[listing[0]].pack(side='bottom')
            key_send = key_send + 1
        # ----------------------------------------------------------------------------------------------------------

        # Packing
        #   Buttons
        self.add_button.pack(side='left')
        self.exit_button.pack(side='left')

        self.prev_button.pack(side='left')
        self.current_date.pack(side='left')
        self.next_button.pack(side='left')

        #   Frames
        self.top_frame.pack(side='top')
        self.existing_frame.pack(side='left')
        self.bottom_frame.pack(side='bottom')

    def manage_entry(self, food_key, listing_key):
        print("function: manage entry")
        print(food_key)
        print(listing_key)

    def add_entry(self):
        print("function: add entry")
        add_entry_GUI = AddEntryWindow(self.food_list, self.entry_diary, self.current_diary)
        self.master.destroy()

    def prev_date(self):
        print("function: prev date")

    def next_date(self):
        print("function: next date")


# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------ Functions -------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
def save_file(food_data, entry_data):
    output_file_food = open('food_data.dat', 'wb')
    pickle.dump(food_data, output_file_food)
    print("Food Data: " + str(food_data))

    output_file_entries = open('entries_data.dat', 'wb')
    pickle.dump(entry_data, output_file_entries)
    print("Entry Diary: " + str(entry_data))


def main():
    try:
        input_file_food = open("food_data.dat", 'rb')
        data_file_food = pickle.load(input_file_food)

        input_file_entries = open("entries_data.dat", 'rb')
        data_file_entries = pickle.load(input_file_entries)
    except(FileNotFoundError, IOError):
        data_file_food = {}
        data_file_entries = {}

    clock = datetime.datetime.now()
    current_date = str(clock.month) + '/' + str(clock.day) + '/' + str(clock.year)
    search = data_file_entries.get(current_date)
    if search is None:
        print("writing new date")
        data_file_entries.update({current_date: []})

    print("data file entries: " + str(data_file_entries))
    root = tkinter.Tk()
    main_gui = MainWindow(root, data_file_food, data_file_entries, current_date)
    root.mainloop()


main()
