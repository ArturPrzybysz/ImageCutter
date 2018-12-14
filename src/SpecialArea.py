class SpecialArea:
    type: str
    area: (int, int, int, int)

    def __init__(self, object_type, area: (int, int, int, int)):
        self.type = object_type
        self.area = area
