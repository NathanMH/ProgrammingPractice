from pynput import keyboard
import tkinter as tk
import json

# Setup
# self.keyfile = open("/home/natha/Documents/keyfile.txt", "a")
with open("C:\\Users\\natha\\Documents\\keyfile.json", "r+") as keyfile:
    key_dict = json.load(keyfile)
# print(key_dict)
global listener


class key_gui:
    def __init__(self, master):

        self.master = master
        master.title("Key Heatmap")

        self.label = tk.Label(master, text="Keymap Tracker!")
        self.label.pack()

        self.greet_button = tk.Button(
            master, text="Start Tracking", command=start_listener
        )
        self.greet_button.place(x=25, y=25)
        self.greet_button.config(width=20, height=4, bg="green")
        self.greet_button.pack()

        self.close_button = tk.Button(master, text="End Tracking", command=end_listener)
        self.close_button.place(x=25, y=50)
        self.close_button.config(width=20, height=4, bg="red")
        self.close_button.pack()


def on_press(key):
    global keystring

    if str(key) in key_dict:
        key_dict[str(key)] += 1
    else:
        key_dict[str(key)] = 1

    print("{0} press".format(key))


def on_release(key):
    print("{0} release".format(key))
    # if key == keyboard.Key.esc:
    # Stop listener
    # print(key_dict)
    # return False


listener = keyboard.Listener(on_press=on_press, on_release=on_release)


def start_listener():
    listener.start()


def end_listener():
    listener.stop()
    with open("C:\\Users\\natha\\Documents\\keyfile.json", "r+") as keyfile:
        keyfile.seek(0)
        keyfile.write(json.dumps(key_dict, indent=4))


root = tk.Tk()
root.geometry("250x200")
my_gui = key_gui(root)
root.mainloop()
