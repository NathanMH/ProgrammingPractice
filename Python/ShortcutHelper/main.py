# -*- coding: utf-8 -*-

import sys

import ShortcutParse

from pathlib import Path

plugindir = Path.absolute(Path(__file__).parent)
paths = (".", "lib", "plugin")
sys.path = [str(plugindir / p) for p in paths] + sys.path

from flowlauncher import FlowLauncher


class Shortcuts(FlowLauncher):
    def test_result(self):
        return [
            {
                "title": "test",
                "subTitle": "subTest",
                "icoPath": "",
                "jsonRPCAction": {"method": "", "parameters": []},
                "score": 0,
            }
        ]

    def get_app_icon(self, app_name):
        return "Images/" + app_name + ".png"

    def get_shortcuts(self, scores):
        scuts = []
        for item in scores:
            temp_obj = {
                "title": item["function"],
                "subTitle": item["keybinding"],
                # "IcoPath": get_app_icon(item["app"]),
                "icoPath": self.get_app_icon(item["app"]),
                "jsonRPCAction": {"method": "", "parameters": []},
                "score": item["score"],
            }
            scuts.append(temp_obj)
        else:
            return scuts

    def query(self, query):

        scored_list = ShortcutParse.main(query)
        return self.get_shortcuts(scored_list)
        # return self.test_result()


if __name__ == "__main__":
    Shortcuts()
    # Test()
