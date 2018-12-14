from src.SpecialArea import SpecialArea


def output_image_name(image_name: str, special_area: SpecialArea):
    seq = (image_name, special_area.type, str(special_area.area))
    return "_".join(seq) + ".jpg"


def _remove_extension(file_name: str):
    arr = file_name.split(".")
    arr.pop()
    return "_".join(arr)
