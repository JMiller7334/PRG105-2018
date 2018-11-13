import tkinter


class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry("250x125")

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.top_label = tkinter.Label(self.top_frame,
                                       text="\n"
                                            "\n"
                                            "\n"
                                            "\n")
        self.show_button = tkinter.Button(self.bottom_frame,
                                          text="Show",
                                          command=self.show)

        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text="Quit",
                                          command=self.quit)

        self.show_button.pack(side="left")
        self.quit_button.pack(side="right")

        self.top_frame.pack()
        self.bottom_frame.pack()

        self.top_label.pack()
        tkinter.mainloop()

    def show(self):
        print("show")
        self.top_label.config(text="Jacob Miller \n"
                                   "8900 US-14 \n"
                                   "Crystal Lake, IL 60012 \n"
                                   "\n")

    def quit(self):
        self.main_window.destroy()


my_gui = MyGui()
