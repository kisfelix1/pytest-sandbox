class BaseProject:
    def __init__(self, name, host, components=None):
        self.name = name
        self.host = host
        self.components = components or {}
