import time
import math
import re
import os
import win32gui
import win32con
import tkinter as tk
import keyboard
# from thefuzz import process

exclude = [
    "Settings",
    "Microsoft Store",
    "Calculator",
    "MainWindow",
    "Program Manager",
    "Microsoft Text Input Application",
    "Nahimic",
    "Windows Input Experience",
]

dirname = os.path.dirname(__file__)

class Program:
    def __init__(self, winTitle, winHwid):
        self.title = winTitle
        self.hwid = winHwid
        self.image = ""

    def set_foreground(self):
        """Show and put the window in the foreground"""
        win32gui.ShowWindow(self.hwid, win32con.SW_RESTORE)
        win32gui.BringWindowToTop(self.hwid)


all_programs = []


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Window Switcher")
        self.root.geometry(self.calc_win_pos())
        self.root.resizable(0, 0)
        self.root.overrideredirect(True)

    def toggle_window(self):
        if self.root.state() == "withdrawn":
            self.root.state("normal")
            self.root.lift()
        else:
            self.root.withdraw()

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
        return "800x64+" + xPosition + "+" + yPosition


class MainFrame(tk.Frame):
    def __init__(self, master=None):
        self.default_image = tk.PhotoImage(
            file= os.path.join(dirname, "filezilla.png")
        )
        super().__init__(master)
        self.master = master
        self.create_search_entry()
        self.pack()

    def search_trace(self, *arg):
        # This is where the fuzzy filter is called
        for window in all_programs:
            rootFrame.create_window_button(window)
        self.update()
        rootWin.update_win_size()
        print(self.fuzzyInput.get())

    def create_search_entry(self):
        # Add command to update list of programs on text change
        self.fuzzyInput = tk.StringVar(rootWin.root, value="Fuzzy Search Here:")
        self.fuzzyInput.trace_add('write', self.search_trace)
        self.fuzzyInputBox = tk.Entry(rootWin.root, font=("Calibri 18"), justify="center", textvariable=self.fuzzyInput)
        self.fuzzyInputBox.pack()
        self.fuzzyInputBox.focus()
        self.fuzzyInputBox.selection_range(0, 'end')

    def create_window_button(self, windObj):
        self.windowButton = tk.Button(
            self,
            image=self.default_image,
            anchor="w",
            compound="left",
            borderwidth=5,
            text=windObj.title,
            width=800,
            height=64,
            command=lambda: windObj.set_foreground(),
        )
        self.windowButton.pack(side="top")

    def get_win_dim(self):
        return self.master.winfo_geometry()


def winEnumHandler(hwnd, ctx):
    if win32gui.IsWindowVisible(hwnd):
        titleStr = win32gui.GetWindowText(hwnd)
        titleId = hwnd
        if titleStr != "" and titleStr not in exclude:
            win = Program(titleStr, titleId)
            # print(titleStr + " : " + titleId)
            all_programs.append(win)


if __name__ == "__main__":

    # Get windows and handles, create window objects
    win32gui.EnumWindows(winEnumHandler, None)

    rootWin = MainWindow()
    rootFrame = MainFrame(master=rootWin.root)

    keyboard.add_hotkey('alt+n', rootWin.toggle_window)
    keyboard.add_hotkey('esc', rootWin.quit_window)

    rootWin.update_win_size()

    # for window in programs:
    #     rootFrame.create_window_button(window)
    rootWin.root.update()
    rootWin.update_win_size()

    rootFrame.mainloop()  # where the frame is created?

    # Hide/show keyboard shortcut
