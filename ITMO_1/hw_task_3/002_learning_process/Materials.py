class Materials:

    def __init__(self, _materials):
        self.materials = _materials

    def __len__(self):
        return len(self.materials)

    def get_materials(self):
        return self.materials