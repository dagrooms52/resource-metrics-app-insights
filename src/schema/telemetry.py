class Telemetry(object):
    
    def __init__(self, name, value, custom_props = None):
        self.name = name
        self.value = value
        self.custom_props = custom_props