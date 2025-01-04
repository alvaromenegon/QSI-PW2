import re

class ShoppingList:
    items: list
    def __init__(self):
        self.items = []

    def validate_item(self, item: str):
        if not isinstance(item, str):
            raise ValueError("Item must be a string")
        if not re.match("^[a-zA-Z0-9 ]+$", item):
            raise ValueError("Item contains invalid characters")

    def add_item(self, item):
        self.validate_item(item)
        self.items.append(item)

    def get_items(self):
        return self.items

    def remove_item(self, item):
        if item not in self.items:
            raise ValueError("Item not in list")
        self.items.remove(item)
    
    def edit_item(self, item, new_item):
        if item not in self.items:
            raise ValueError("Item not in list")
        self.validate_item(new_item)
        self.items[self.items.index(item)] = new_item

    def clear(self):
        self.items = []