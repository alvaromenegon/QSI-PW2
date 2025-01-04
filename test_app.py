import pytest
from app import ShoppingList


def test_create_list():
    shopping_list = ShoppingList()
    assert isinstance(shopping_list, ShoppingList)
    assert shopping_list.get_items() == []


def test_add_item():
    shopping_list = ShoppingList()
    shopping_list.add_item("Milk")
    assert "Milk" in shopping_list.get_items()


def test_add_item_invalid_characters():
    shopping_list = ShoppingList()
    with pytest.raises(ValueError, match="Item contains invalid characters"):
        shopping_list.add_item("Milk$")


def test_add_item_invalid_type():
    shopping_list = ShoppingList()
    with pytest.raises(ValueError, match="Item must be a string"):
        shopping_list.add_item(1)


def test_get_items():
    shopping_list = ShoppingList()
    shopping_list.add_item("Milk")
    shopping_list.add_item("Bread")
    assert shopping_list.get_items() == ["Milk", "Bread"]


def test_remove_item():
    shopping_list = ShoppingList()
    shopping_list.add_item("Milk")
    shopping_list.remove_item("Milk")
    assert "Milk" not in shopping_list.get_items()


def test_remove_item_not_in_list():
    shopping_list = ShoppingList()
    shopping_list.add_item("Milk")
    with pytest.raises(ValueError, match="Item not in list"):
        shopping_list.remove_item("Bread")


def test_edit_item():
    shopping_list = ShoppingList()
    shopping_list.add_item("Milk")
    shopping_list.edit_item("Milk", "Almond Milk")
    assert "Milk" not in shopping_list.get_items()
    assert "Almond Milk" in shopping_list.get_items()


def test_edit_item_not_in_list():
    shopping_list = ShoppingList()
    shopping_list.add_item("Milk")
    with pytest.raises(ValueError, match="Item not in list"):
        shopping_list.edit_item("Bread", "Almond Milk")


def test_clear():
    shopping_list = ShoppingList()
    shopping_list.add_item("Milk")
    shopping_list.add_item("Bread")
    shopping_list.clear()
    assert shopping_list.get_items() == []
