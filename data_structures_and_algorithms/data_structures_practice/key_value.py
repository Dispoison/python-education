class KeyValue:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"{repr(self.key)}: {repr(self.value)}"

    def __eq__(self, other):
        return self.key == other.key if isinstance(other, KeyValue) else self.key == other
