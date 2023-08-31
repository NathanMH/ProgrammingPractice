import re
import os
import subprocess
import sys
from turtle import textinput

dirname = os.path.dirname(__file__)

# Need to run "C:\Users\natha\Desktop\PortableUtils\ControlMyMonitor\ControlMyMonitor.exe /smonitors monitors.txt
monitor_file = dirname + "monitors.txt"
monitor_filepath = (
    "C:\\Users\\natha\\Desktop\\PortableUtils\\ControlMyMonitor\\monitors.txt"
)

monitor_strings = []
monitors = {
    "lenovo": '"U511G8F2"',
    "viewsonic1": '"UPN171702003"',
    "viewsonic2": '"UPN171701939"',
}


def get_monitor_strings():
    with open(monitor_filepath, "r", encoding="utf16") as f:
        for line in f:
            # if re.search(r"DISPLAY", line):
            data = re.search(r"\\\\\.\\DISPLAY\d\\Monitor\d", line)
            if data is not None:
                monitor_strings.append(data.group())


def get_monitor_names():
    with open(monitor_filepath, "r", encoding="utf16") as f:
        for line in f:
            if re.search(r"Monitor ID", line):
                data = re.search(r'"(.+?)"', line)
                monitor_strings.append(data.group())


def get_monitor_serials():
    with open(monitor_filepath, "r", encoding="utf16") as f:
        for line in f:
            if re.search(r"Serial", line):
                data = re.search(r'"(.+?)"', line)
                monitor_strings.append(data.group())


def set_bright(level):
    command_string = "C:\\Users\\natha\\Desktop\\PortableUtils\\ControlMyMonitor\\ControlMyMonitor.exe /SetValue "
    for mon in monitors.values():
        full_command = command_string + mon + " 10 " + str(level)
        print(full_command)

        subprocess.run(full_command, shell=True)


def switch_input(mon):
    command_string = "C:\\Users\\natha\\Desktop\\PortableUtils\\ControlMyMonitor\\ControlMyMonitor.exe /SwitchValue "
    full_command = command_string + mon + " 60 49 15"
    print(full_command)
    subprocess.run(full_command, shell=True)


if __name__ == "__main__":

    try:
        # print(sys.argv[1])
        # print(sys.argv[2])

        if sys.argv[1] == "lenovo" and sys.argv[2] == "switch":
            switch_input(monitors["lenovo"])
        elif sys.argv[1] == "brightness":
            brightness = textinput("Brightness", "Enter brightness:")
            set_bright(brightness)
    except IndexError:
        print("no args")

    # set_max_bright()
