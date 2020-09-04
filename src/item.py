

class Item:
    def __init__(self, name, description):  # what things could this have? properties?
        self.name = name
        self.description = description


class Tool(Item):
    def __init__(self):
        pass


# Weapon is_a Item
class Weapon(Item):
    def __init__(self):  # what properties would we use here? damage, powers, etc..?
        pass


# Treasure is_a Item
class Treasure(Item):
    def __init__(self):  # what properties could you have in this init function?
        pass
