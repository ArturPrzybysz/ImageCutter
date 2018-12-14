from config import ROOT_DIR
import os

from src.ImageCutter import ImageCutter
from src.Parser import Parser

xml_directory = os.path.join(ROOT_DIR, "data", "labels")
img_directory = os.path.join(ROOT_DIR, "data", "images")
out_directory = os.path.join(ROOT_DIR, "data", "output")

directory = os.fsencode(xml_directory)

for file in os.listdir(directory):
    file_path = os.path.join(xml_directory, os.fsdecode(file))
    image_info = Parser.parse(file_path)
    ImageCutter.cut(image_info, img_directory, out_directory)
