"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section that explain the required code
    Your file should compile error free
    Submit your completed file
"""
import tkinter
import tkinter.messagebox


# TODO 13.2 Using the tkinter Module
# Write the code from program 13-2 to display an empty window, no need
# to re-import tkinter
def main():
    tkinter.Tk()
    tkinter.mainloop()


main()


# create the class MyGUI2
class MyGui2:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # TODO 13.3 Adding a label widget
        # add a label that prints your first and last name
        self.label = tkinter.Label(self.main_window,
                                   text="Jacob Miller")
        # pack the label
        self.label.pack()
        # enter the main loop
        tkinter.mainloop()


# create an instance of MyGUI2
my_gui2 = MyGui2()


# TODO 13.4 Organizing Widgets with Frames
class MyGui3:
    def __init__(self):
        self.main_window = tkinter.Tk()
        # Create a window in the MyGUI3 class that has two frames
        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        # In the top Frame add a labels with your name and major
        self.label1 = tkinter.Label(self.frame1,
                                    text="Jacob Miller | Mobil Design & Development")
        self.label1.pack(side='top')
        # In the bottom frame add labels with the classes you are taking this semester
        self.label2 = tkinter.Label(self.frame2,
                                    text="PRG 105 | DGM 107 | GRA 167")
        self.label2.pack(side='top')

        self.frame1.pack()  # NOTE: packing frames is important for them to show up.
        self.frame2.pack()

        tkinter.mainloop()


my_gui3 = MyGui3()


# TODO 13.5 Button Widgets and info Dialog Boxes
# Tell a joke with a button to show the punch line, which should appear in a dialog box

class MyGui4:
    def __init__(self):
        self.avoid_static_error = 0
        self.main_window = tkinter.Tk()
        self.button = tkinter.Button(self.main_window,
                                     text="Why did the the chicken cross the road?",
                                     command=self.on_clicked)
        self.button.pack()
        tkinter.mainloop()

    def on_clicked(self):
        self.avoid_static_error += 1
        tkinter.messagebox.showinfo('Response', 'To get to the other side...')


my_gui4 = MyGui4()


# TODO 13.6 getting input / 13.7 Using Labels as output fields
# Using the program in 13.10 kilo converter as a sample, create a program
# to convert inches to centimeters
class MyGui5:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.top_label = tkinter.Label(self.top_frame,
                                       text="Please enter inches to be converted to centimeters below.")
        self.user_entry = tkinter.Entry(self.top_frame, width=10)

        self.top_label.pack(side="left")
        self.user_entry.pack(side="left")

        self.main_button = tkinter.Button(self.bottom_frame,
                                          text="convert",
                                          command=self.convert)

        self.main_button.pack()
        self.top_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()

    def convert(self):
        entry = float(self.user_entry.get())
        total = float(entry * 2.54)
        tkinter.messagebox.showinfo("Response", "" + str(entry) + "in is equal to " + str(total) + "cm.")


my_gui5 = MyGui5()
