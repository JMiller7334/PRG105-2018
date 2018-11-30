import tkinter
import pickle
import datetime


class AddEntryWindow:
    def __init__(self, food_data, entry_data):
        self.root = tkinter.Tk()
        self.root.title("Entry Management")

        # Variables
        self.food_list = food_data
        self.entry_list = entry_data

        # Frames
        self.creation_frame = tkinter.Frame(self.root)
        self.existing_frame = tkinter.Frame(self.root)

        # Creation Frame
        #   Buttons/interactive/Labels
        self.new_name_label = tkinter.Label(self.creation_frame, text='Food name: ')
        self.new_name_entry = tkinter.Entry(self.creation_frame, width=10)
        self.new_serving_label = tkinter.Label(self.creation_frame, text='Serving size information: ')
        self.new_serving_entry = tkinter.Entry(self.creation_frame, width=10)
        self.new_kcal_label = tkinter.Label(self.creation_frame, text='Kcal per serving: ')
        self.new_kcal_entry = tkinter.Entry(self.creation_frame, width=4)
        self.new_carb_label = tkinter.Label(self.creation_frame, text='Carbs per serving: ')
        self.new_carb_entry = tkinter.Entry(self.creation_frame, width=3)
        self.new_fat_label = tkinter.Label(self.creation_frame, text='Fats per serving: ')
        self.new_fat_entry = tkinter.Entry(self.creation_frame, width=3)
        self.new_protein_label = tkinter.Label(self.creation_frame, text='Protein per serving: ')
        self.new_protein_entry = tkinter.Entry(self.creation_frame, width=3)
        self.create_button = tkinter.Button(self.creation_frame, text='Create Food', command=self.create_food)
        self.back_button = tkinter.Button(self.creation_frame, text='Go Back', command=self.go_back)

        # Existing Frame
        self.existing_info_label = tkinter.Label(self.existing_frame, text='Existing foods are listed below')

        # Packing
        #   Existing Frame
        self.existing_info_label.pack(side='top')

        #   Creation Frame
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

    def create_food(self):
        print("function: create food")

    def go_back(self):
        print("function: go back")
        save_file(self.food_list, self.entry_list)
        main_gui = MainWindow(tkinter.Tk(), self.food_list, self.entry_list)
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
