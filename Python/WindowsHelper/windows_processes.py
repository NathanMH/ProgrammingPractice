import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_window_widget("Test title1")
        self.create_window_widget("Test title2")
        self.create_window_widget("Test title3")

    def create_window_widget(self, title):
        null_image = tk.PhotoImage(width=0, height=0)
        self.windowButton = tk.Button(self, text=title, width="750", height="50",
                                      image=null_image, compound="center", borderwidth=0)
        self.windowButton.pack()


        # self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        # self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
root.title("Window Switcher")
root.geometry("800x400")
root.resizable(0,0)

app = Application(master=root)
app.mainloop()
