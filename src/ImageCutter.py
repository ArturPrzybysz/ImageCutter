import os
from PIL import Image
from src.ImageInfo import ImageInfo
from src.SpecialArea import SpecialArea
from src.util import output_image_name


class ImageCutter:
    @staticmethod
    def cut(image_info: ImageInfo, img_directory: str, output_directory: str):
        image_path = os.path.join(img_directory, image_info.image_name)
        image = Image.open(image_path)
        for special_area in image_info.special_areas:
            name = output_image_name(image_info.image_name, special_area)
            address = os.path.join(output_directory, name)
            ImageCutter._save_area(image, special_area, address)

    @staticmethod
    def _save_area(image, special_area: SpecialArea, output_address: str):
        cropped_image = image.crop(special_area.area)
        cropped_image_address = os.path.join(output_address)
        cropped_image.save(cropped_image_address)
