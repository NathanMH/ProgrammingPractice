import xml.etree.ElementTree as ET
import json
import time

apple_filepath = r"C:\Users\natha\iCloudDrive\Health\apple_health_export\export.xml"
nomie_filepath = r"C:\Users\natha\iCloudDrive\Health\nomie-5.6.4-2022-07-22-19_23.json"


def nomie_json_parse():
    with open(nomie_filepath, "r", encoding="utf8") as nomie_json:
        nomie_data = json.load(nomie_json)
        # print(nomie_data)
        print(nomie_data["events"][0])


def apple_xml_parse():

    with open(apple_filepath, "r") as health_xml:
        tree = ET.parse(health_xml)
        root = tree.getroot()
        print("Root:")
        print(root)
        print(root[0])
        print(root[1].tag)
        print(root[2].attrib)
        print(root[2].attrib["sourceName"])
        for child in root:
            print(child)
            try:
                if child.attrib["sourceName"] == "Hidrate":
                    print(child.attrib)
            except:
                print("header row?")
            time.sleep(1)


if __name__ == "__main__":
    nomie_json_parse()
