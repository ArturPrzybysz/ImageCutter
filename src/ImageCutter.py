import os
import xml.etree.ElementTree as ET


class XMLParser:
    @staticmethod
    def parse(img_directory: str, xml_directory: str, output_directory: str):
        directory = os.fsencode(xml_directory)

        for file in os.listdir(directory):
            file_path = os.path.join(xml_directory, os.fsdecode(file))
            tree = ET.parse(file_path)
            root = tree.getroot()[0]

    @staticmethod
    def _parse_file():
        pass
