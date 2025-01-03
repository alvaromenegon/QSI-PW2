import pytest
from app import ShoppingList, create_list, add_item, get_items, remove_item, edit_item, clear

def test_create_list():
    shopping_list = create_list()
    assert isinstance(shopping_list, ShoppingList)
    assert shopping_list.get_items() == []

def test_add_item():
    shopping_list = create_list()
    add_item(shopping_list, "Milk")
    assert "Milk" in shopping_list.get_items()

def test_add_item_invalid_characters():
    shopping_list = create_list()
    with pytest.raises(ValueError, match="Item contains invalid characters"):
        add_item(shopping_list, "Milk$")

def test_add_item_invalid_type():
    shopping_list = create_list()
    with pytest.raises(ValueError, match="Item must be a string"):
        add_item(shopping_list, 1)

def test_get_items():
    shopping_list = create_list()
    add_item(shopping_list, "Milk")
    add_item(shopping_list, "Bread")
    assert get_items(shopping_list=shopping_list) == ["Milk", "Bread"]

def test_remove_item():
    shopping_list = create_list()
    add_item(shopping_list, "Milk")
    remove_item(shopping_list, "Milk")
    assert "Milk" not in shopping_list.get_items()
    
def test_remove_item_not_in_list():
    shopping_list = create_list()
    add_item(shopping_list, "Milk")
    with pytest.raises(ValueError, match="Item not in list"):
        remove_item(shopping_list, "Bread")

def test_edit_item():
    shopping_list = create_list()
    add_item(shopping_list, "Milk")
    edit_item(shopping_list, "Milk", "Almond Milk")
    assert "Milk" not in shopping_list.get_items()
    assert "Almond Milk" in shopping_list.get_items()

def test_edit_item_not_in_list():
    shopping_list = create_list()
    add_item(shopping_list, "Milk")
    with pytest.raises(ValueError, match="Item not in list"):
        edit_item(shopping_list, "Bread", "Almond Milk")

def test_clear():
    shopping_list = create_list()
    add_item(shopping_list, "Milk")
    add_item(shopping_list, "Bread")
    clear(shopping_list)
    assert shopping_list.get_items() == []