import time
import math
import re
import win32gui
import win32con
import tkinter as tk
import keyboard

exclude = [
    "Settings",
    "Microsoft Store",
    "Calculator",
    "MainWindow",
    "Program Manager",
    "Microsoft Text Input Application",
]
titles = {}


def winEnumHandler(hwnd, ctx):
    if win32gui.IsWindowVisible(hwnd):
        titleStr = win32gui.GetWindowText(hwnd)
        titleId = hwnd
        if titleStr != "" and titleStr not in exclude:
            # print(titleStr + " : " + titleId)
            titles[titleStr] = titleId


win32gui.EnumWindows(winEnumHandler, None)


def set_foreground(handle):
    """Show and put the window in the foreground"""
    win32gui.ShowWindow(handle, win32con.SW_RESTORE)
    win32gui.BringWindowToTop(handle)


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.default_image = tk.PhotoImage(
            file="C:\\Users\\natha\\Desktop\\Documents\\Python_Projects\\WindowsSwitcher\\filezilla.png"
        )

        for title, titleId in titles.items():
            print(title + ": " + str(titleId))
            # frameHeight += 200
            self.create_window_widget(title, titleId)

        tk.Entry(self, textvariable=userInput).pack()
        tk.Button(
            self,
            text="Quit",
            command=quit_window,
            fg="white",
            bg="black",
            width=20,
        ).pack(pady=20)

    def create_window_widget(self, title, titleId):
        self.windowButton = tk.Button(
            self,
            image=self.default_image,
            anchor="w",
            compound="left",
            borderwidth=5,
            text=title,
            width=800,
            height=64,
            command=lambda: self.focus(titleId),
        )
        self.windowButton.pack(side="top")

    def focus(self, titleId):
        # Find and focus a window
        set_foreground(titleId)


def toggle_window():
    if root.state() == "withdrawn":
        root.state("normal")
    else:
        root.withdraw()


def quit_window():
    root.destroy()


def calc_win_size(root):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    xPosition = str(math.floor(screenwidth / 2 - 400))
    yPosition = str(math.floor(screenheight / 3))
    frameHeight = 200
    return "800x200+" + xPosition + "+" + yPosition


if __name__ == "__main__":

    root = tk.Tk()
    root.title("Window Switcher")
    root.geometry(calc_win_size(root))
    root.resizable(0, 0)
    root.overrideredirect(True)

    # Hide/show keyboard shortcut
    keyboard.add_hotkey("alt + space", toggle_window)
    keyboard.add_hotkey("escape", quit_window)
    userInput = tk.StringVar()

    app = Application(master=root)
    app.mainloop()
    print(userInput.get())

# for title, handle in titles.items():
#     print(title + ": " + str(handle))

# win32gui.SetForegroundWindow(titles["This PC"])
