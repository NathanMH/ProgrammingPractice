import math
import os
import keyboard
import ShortcutParser
import sys

# from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2 import QtCore
from PySide2 import QtWidgets

dirname = os.path.dirname(__file__)
shortcuts_list = dirname


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUI()
        self.move(QtWidgets.QDesktopWidget().availableGeometry().center())

    def initUI(self):
        # self.statusBar().showMessage("Ready")
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.inputTextLabel = QtWidgets.QLabel()

        self.hbox = QtWidgets.QHBoxLayout()
        self.hbox.addStretch(1)

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addStretch(1)

        self.vbox.addLayout(self.hbox)

        self.make_fuzzy_search()

        self.vbox.addWidget(self.inputTextLabel)

        self.setLayout(self.vbox)

        self.fuzzyInput.textChanged.connect(self.make_fuzzy_list)

        self.show()

    def make_fuzzy_search(self):
        self.fuzzyInput = QtWidgets.QLineEdit()
        self.vbox.addWidget(self.fuzzyInput)

    def make_app_labels(self):
        self.app_label1 = QtWidgets.QLabel

    def make_fuzzy_list(self):
        print(self.fuzzyInput.text())
        self.results = ShortcutParser.make_scores(self.fuzzyInput.text())
        # print(self.results)
        self.inputTextLabel.setText(self.results[0]["application"])

    # show hide window function
    def toggle_window(self):
        return

    def quit_window(self):
        return


if __name__ == "__main__":

    ShortcutParser.create_single_string()

    app = QtWidgets.QApplication(sys.argv)
    ex = MainWindow()
    app.exec_()
    # ShortcutParser.create_single_string()
    # shorts = ShortcutParser.make_scores("buffer")
    # print(shorts)

    # Hide/show keyboard shortcut
