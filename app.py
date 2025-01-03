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
    
def create_list() -> ShoppingList:
    return ShoppingList()

def add_item(shopping_list: ShoppingList, item: str):
    shopping_list.add_item(item)

def get_items(shopping_list: ShoppingList):
    return shopping_list.get_items()

def remove_item(shopping_list: ShoppingList, item: str):
    shopping_list.remove_item(item)

def edit_item(shopping_list: ShoppingList, item: str, new_item: str):
    shopping_list.edit_item(item, new_item)

def clear(shopping_list: ShoppingList):
    shopping_list.clear()