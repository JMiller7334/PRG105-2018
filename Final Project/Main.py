import tkinter
import pickle


class MainWindow:
    def __init__(self, master, food_data, entry_data):
        self.master = master
        self.master.title("Fitness Tracker")

        # Variables
        self.food_list = food_data
        self.entry_list = entry_data

        # Frames
        bottom_frame = tkinter.Frame(self.master)

        # Pack Frames
        bottom_frame.pack(side='bottom')



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
