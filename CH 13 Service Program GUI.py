import tkinter
import tkinter.messagebox


class MainGui:
    def __init__(self):
        self.total = 0
        self.receipt = "Items Purchased\n"

        self.root = tkinter.Tk()
        self.root.geometry("725x300")

        # Gui Frames
        self.high_frame = tkinter.Frame(self.root)
        self.low_frame = tkinter.Frame(self.root)

        # Gui Labels
        self.title_label = tkinter.Label(self.high_frame,
                                         text="Food Shop")

        # Default checkbox settings
        self.cb_var1 = tkinter.IntVar()
        self.cb_var1.set(0)
        self.cb_var2 = tkinter.IntVar()
        self.cb_var2.set(0)
        self.cb_var3 = tkinter.IntVar()
        self.cb_var3.set(0)
        self.cb_var4 = tkinter.IntVar()
        self.cb_var4.set(0)
        self.cb_var5 = tkinter.IntVar()
        self.cb_var5.set(0)
        self.cb_var6 = tkinter.IntVar()
        self.cb_var6.set(0)
        self.cb_var7 = tkinter.IntVar()
        self.cb_var7.set(0)

        # Gui CheckBoxes
        self.checkbox_1 = tkinter.Checkbutton(self.high_frame,
                                              text="bread | cost: $1.15",
                                              variable=self.cb_var1)
        self.checkbox_2 = tkinter.Checkbutton(self.high_frame,
                                              text="12 eggs | cost: $2.25",
                                              variable=self.cb_var2)
        self.checkbox_3 = tkinter.Checkbutton(self.high_frame,
                                              text="bottle of water | cost: $0.95",
                                              variable=self.cb_var3)
        self.checkbox_4 = tkinter.Checkbutton(self.high_frame,
                                              text="apple | cost: $0.99",
                                              variable=self.cb_var4)
        self.checkbox_5 = tkinter.Checkbutton(self.high_frame,
                                              text="banana | cost: $0.45",
                                              variable=self.cb_var5)
        self.checkbox_6 = tkinter.Checkbutton(self.high_frame,
                                              text="cake | cost: $9.99",
                                              variable=self.cb_var6)
        self.checkbox_7 = tkinter.Checkbutton(self.high_frame,
                                              text="fried chicken | cost: $7.99",
                                              variable=self.cb_var7)

        # Gui Buttons
        self.purchase_button = tkinter.Button(self.low_frame,
                                              text="purchase",
                                              command=self.purchase)
        self.quit_button = tkinter.Button(self.low_frame,
                                          text="quit",
                                          command=self.root.destroy)

        # Pack Gui
        self.title_label.pack(side="top")

        self.checkbox_1.pack()
        self.checkbox_2.pack()
        self.checkbox_3.pack()
        self.checkbox_4.pack()
        self.checkbox_5.pack()
        self.checkbox_6.pack()
        self.checkbox_7.pack()

        self.purchase_button.pack(side="right")
        self.quit_button.pack(side="left")

        self.high_frame.pack(side="top")
        self.low_frame.pack(side="bottom")

        # Main Loop
        tkinter.mainloop()

    def purchase(self):
        self.receipt = self.receipt + "\n"

        if self.cb_var1.get() == 1:
            self.total = self.total + 1.15
            self.receipt = self.receipt + "bread | $1.15\n"

        if self.cb_var2.get() == 1:
            self.total = self.total + 1.25
            self.receipt = self.receipt + "12 eggs | $1.15\n"

        if self.cb_var3.get() == 1:
            self.total = self.total + 0.95
            self.receipt = self.receipt + "bottle of water | $0.95\n"

        if self.cb_var4.get() == 1:
            self.total = self.total + 0.99
            self.receipt = self.receipt + "apple | $0.99\n"

        if self.cb_var5.get() == 1:
            self.total = self.total + 0.45
            self.receipt = self.receipt + "banana | $0.45\n"

        if self.cb_var6.get() == 1:
            self.total = self.total + 9.99
            self.receipt = self.receipt + "cake | $9.99\n"

        if self.cb_var7.get() == 1:
            self.total = self.total + 7.99
            self.receipt = self.receipt + "fried chicken | $7.99\n"

        new_total = format(self.total, ",.2f")
        self.receipt = self.receipt + "\n"
        self.receipt = self.receipt + "Your total: $" + str(new_total)
        tkinter.messagebox.showinfo("receipt", str(self.receipt))


gui = MainGui()
