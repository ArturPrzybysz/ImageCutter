class ImageInfo:
    size: (int, int)
    image_name: str
    special_areas: []

    def __init__(self, size, image_name, special_areas):
        self.size = size
        self.image_name = image_name
        self.special_areas = special_areas
