import xml.etree.ElementTree as ET

from src.ImageInfo import ImageInfo

from src.SpecialArea import SpecialArea


class Parser:
    @staticmethod
    def parse(xml_location: str):
        tree = ET.parse(xml_location)
        root = tree.getroot()

        size = Parser._get_size(root)
        img_name = Parser._get_img_name(root)
        special_areas = Parser._get_special_areas(root)

        return ImageInfo(size, img_name, special_areas)

    @staticmethod
    def _get_size(root):
        width = int(root.find("./size/width").text)
        height = int(root.find(".size/height").text)
        return width, height

    @staticmethod
    def _get_img_name(root):
        return root.find("./filename").text

    @staticmethod
    def _get_special_areas(root):
        special_areas = []
        for obj in root.findall('object'):
            object_type = obj.find("./name").text
            x_min = int(obj.find("./bndbox/xmin").text)
            y_min = int(obj.find("./bndbox/ymin").text)
            x_max = int(obj.find("./bndbox/xmax").text)
            y_max = int(obj.find("./bndbox/ymax").text)

            special_areas.append(SpecialArea(object_type, (x_min, y_min, x_max, y_max)))
        return special_areas
