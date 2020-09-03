# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Item:
    def __init__(self):  # what things could this have? properties?
        pass


# Weapon is_a Item
class Weapon(Item):
    def __init__(self):  # what properties would we use here? damage, powers, etc..?
        pass


# Treasure is_a Item
class Treasure(Item):
    def __init__(self):  # what properties could you have in this init function?
        pass
