import math
import re
import os
import tkinter as tk
from tkinter import ttk

# import keyboard
from global_hotkeys import *
import pystray
from pystray import MenuItem as item
from PIL import Image
import ShortcutParser

dirname = os.path.dirname(__file__)
shortcuts_list = dirname


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Shortcut Helper")
        self.root.geometry(self.calc_win_pos())
        self.root.resizable(0, 0)
        self.root.overrideredirect(True)

    def toggle_window(self):
        if self.root.state() == "withdrawn":
            self.root.state("normal")
            self.root.lift()
        else:
            self.root.withdraw()

        # image = Image.open(os.path.join(dirname, "filezilla.png"))
        # menu = (item("Quit", print("Quit")), item("Show", print("show")))
        # icon = pystray.Icon("name", image, "My System Tray Icon", menu)
        # icon.run()

    def quit_window(self):
        self.root.destroy()

    def update_win_size(self):
        # Get current size, parse and update (64 is the icon size)
        currGeo = re.search(r"(?<=x)\d*(?=\+)", self.root.winfo_geometry()).group(0)
        newGeo = "800x" + str(int(currGeo) + 68)

        self.root.geometry(newGeo)
        self.root.update()

    def calc_win_pos(self):
        # Place the windows in the center of the screen
        xPosition = str(math.floor(self.root.winfo_screenwidth() / 2 - 400))
        yPosition = str(math.floor(self.root.winfo_screenheight() / 3))
        return "763x373+" + xPosition + "+" + yPosition  # 64 * 5 + 64


class MainFrame(ttk.Frame):
    def __init__(self, master=None):
        self.default_image = tk.PhotoImage(file=os.path.join(dirname, "filezilla.png"))
        self.zero_img = tk.PhotoImage()  # Zero size img so labels can be in pixels
        super().__init__(master)
        self.master = master
        # self.create_search_entry()

        self.grid()
        self.make_app_labels()
        self.make_desc_labels()
        self.make_sc_labels()
        self.create_search_entry()
        self.add_labels()

    def add_labels(self):
        self.fuzzyInputBox.grid(column=0, row=0, columnspan=3)
        self.app_label0.grid(column=0, row=1)
        self.app_label1.grid(column=0, row=2)
        self.app_label2.grid(column=0, row=3)
        self.app_label3.grid(column=0, row=4)
        self.app_label4.grid(column=0, row=5)
        self.sc_label0.grid(column=1, row=1)
        self.sc_label1.grid(column=1, row=2)
        self.sc_label2.grid(column=1, row=3)
        self.sc_label3.grid(column=1, row=4)
        self.sc_label4.grid(column=1, row=5)
        self.desc_label0.grid(column=2, row=1)
        self.desc_label1.grid(column=2, row=2)
        self.desc_label2.grid(column=2, row=3)
        self.desc_label3.grid(column=2, row=4)
        self.desc_label4.grid(column=2, row=5)

    def make_app_labels(self):
        self.app_label0 = tk.Label(
            self,
            text="label0",
            image=self.default_image,
            compound="left",
            borderwidth=1,
            relief="solid",
            width=150,
            anchor="w",
        )
        self.app_label1 = tk.Label(
            self,
            text="label1",
            image=self.default_image,
            compound="left",
            borderwidth=1,
            relief="solid",
            width=150,
            anchor="w",
        )
        self.app_label2 = tk.Label(
            self,
            text="label2",
            image=self.default_image,
            compound="left",
            borderwidth=1,
            relief="solid",
            width=150,
            anchor="w",
        )
        self.app_label3 = tk.Label(
            self,
            text="label3",
            image=self.default_image,
            compound="left",
            borderwidth=1,
            relief="solid",
            width=150,
            anchor="w",
        )
        self.app_label4 = tk.Label(
            self,
            text="another label4",
            image=self.default_image,
            compound="left",
            borderwidth=1,
            relief="solid",
            width=150,
            anchor="w",
        )

    def make_sc_labels(self):
        self.sc_label0 = tk.Label(
            self,
            text="This is the shortcut",
            image=self.zero_img,
            compound="left",
            borderwidth=1,
            relief="solid",
            width=200,
            height=64,
        )
        self.sc_label1 = tk.Label(
            self,
            text="This is the shortcut",
            image=self.zero_img,
            compound="left",
            borderwidth=1,
            relief="solid",
            width=200,
            height=64,
        )
        self.sc_label2 = tk.Label(
            self,
            text="This is the shortcut",
            image=self.zero_img,
            compound="left",
            borderwidth=1,
            relief="solid",
            width=200,
            height=64,
        )
        self.sc_label3 = tk.Label(
            self,
            text="This is the shortcut",
            image=self.zero_img,
            compound="left",
            borderwidth=1,
            relief="solid",
            width=200,
            height=64,
        )
        self.sc_label4 = tk.Label(
            self,
            text="This is the shortcut",
            image=self.zero_img,
            compound="left",
            borderwidth=1,
            relief="solid",
            width=200,
            height=64,
        )

    def make_desc_labels(self):
        self.desc_label0 = tk.Label(
            self,
            text="desc0",
            image=self.zero_img,
            compound="left",
            borderwidth=1,
            relief="solid",
            width=400,
            height=64,
        )
        self.desc_label1 = tk.Label(
            self,
            text="a desc",
            image=self.zero_img,
            compound="left",
            borderwidth=1,
            relief="solid",
            width=400,
            height=64,
        )
        self.desc_label2 = tk.Label(
            self,
            text="desc2",
            image=self.zero_img,
            compound="left",
            borderwidth=1,
            relief="solid",
            width=400,
            height=64,
        )
        self.desc_label3 = tk.Label(
            self,
            text="desc3",
            image=self.zero_img,
            compound="left",
            borderwidth=1,
            relief="solid",
            width=400,
            height=64,
        )
        self.desc_label4 = tk.Label(
            self,
            text="no text",
            image=self.zero_img,
            compound="left",
            borderwidth=1,
            relief="solid",
            width=400,
            height=64,
        )

    def search_trace(self, *arg):
        # This is where the fuzzy filter is called
        results = ShortcutParser.make_scores(self.fuzzyInput.get())
        self.app_label0.configure(text=results[0]["application"])
        self.app_label1.configure(text=results[1]["application"])
        self.app_label2.configure(text=results[2]["application"])
        self.app_label3.configure(text=results[3]["application"])
        self.app_label4.configure(text=results[4]["application"])
        self.sc_label0.configure(text=results[0]["keybinding"])
        self.sc_label1.configure(text=results[1]["keybinding"])
        self.sc_label2.configure(text=results[2]["keybinding"])
        self.sc_label3.configure(text=results[3]["keybinding"])
        self.sc_label4.configure(text=results[4]["keybinding"])
        self.desc_label0.configure(text=results[0]["function"])
        self.desc_label1.configure(text=results[1]["function"])
        self.desc_label2.configure(text=results[2]["function"])
        self.desc_label3.configure(text=results[3]["function"])
        self.desc_label4.configure(text=results[4]["function"])
        # print(self.fuzzyInput.get())
        self.update()

    def create_search_entry(self):
        # Add command to update list of programs on text change
        self.fuzzyInput = tk.StringVar(rootWin.root, value="Fuzzy Search Here:")
        self.fuzzyInput.trace_add("write", self.search_trace)
        self.fuzzyInputBox = ttk.Entry(
            self, font=("Calibri 18"), textvariable=self.fuzzyInput, width=36
        )
        self.fuzzyInputBox.focus()
        self.fuzzyInputBox.selection_range(0, "end")

    def get_win_dim(self):
        return self.master.winfo_geometry()


if __name__ == "__main__":

    ShortcutParser.create_single_string()
    # shorts = ShortcutParser.make_scores("buffer")

    # tk.Widget.tk.call("source", "azure.tcl")
    # tk.Widget.tk.call("set_theme", "dark")

    rootWin = MainWindow()
    rootFrame = MainFrame(master=rootWin.root)

    rootFrame.tk.call("source", "azure.tcl")
    rootFrame.tk.call("set_theme", "dark")

    def unhide_focus():
        rootWin.toggle_window()
        rootFrame.fuzzyInputBox.focus_force()
        rootFrame.fuzzyInputBox.selection_range(0, "end")

    # Hide/show keyboard shortcut
    bindings = [[["alt", "n"], None, unhide_focus]]
    register_hotkeys(bindings)
    start_checking_hotkeys()

    # keyboard.add_hotkey("ctrl+insert", unhide_focus)
    # keyboard.add_hotkey("esc", rootWin.quit_window)

    rootFrame.mainloop()  # where the frame is created?
