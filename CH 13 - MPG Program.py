import tkinter


class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry("250x125")

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.gallons_label = tkinter.Label(self.top_frame,
                                           text="Enter total gallons below")
        self.gallons_entry = tkinter.Entry(self.top_frame, width=10)

        self.miles_label = tkinter.Label(self.top_frame,
                                         text="Enter total miles traveled below")
        self.miles_entry = tkinter.Entry(self.top_frame, width=10)

        self.total_label = tkinter.Label(self.top_frame,
                                         text="Miles per gallon: nil")

        self.convert_button = tkinter.Button(self.bottom_frame,
                                             text="convert",
                                             command=self.convert)

        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text="Quit",
                                          command=self.quit)

        self.convert_button.pack(side="left")
        self.quit_button.pack(side="right")

        self.top_frame.pack()
        self.bottom_frame.pack(side="bottom")

        self.gallons_label.pack()
        self.gallons_entry.pack()
        self.miles_label.pack()
        self.miles_entry.pack()
        self.total_label.pack()

        tkinter.mainloop()

    def convert(self):
        gallons = float(self.gallons_entry.get())
        miles = float(self.miles_entry.get())
        total = miles / gallons
        self.total_label.config(text="Miles Per Gallon: " + str(total))

    def quit(self):
        self.main_window.destroy()


my_gui = MyGui()
