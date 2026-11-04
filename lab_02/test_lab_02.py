from lab_02 import add_logic, delete_logic, update_logic

def test_add_logic():
    test_list = []
    add_logic(test_list, "Zak", "111", "19", "Zak@uni")
    add_logic(test_list, "Bob", "222", "18", "bob@uni")

    assert len(test_list) == 2
    assert test_list[0]["name"] == "Bob"
    assert test_list[1]["name"] == "Zak"

def test_delete_logic():
    test_list = [{"name": "Bob", "phone": "111", "age": "20", "email": "bob@uni"}]

    pos = delete_logic(test_list, "Bob")
    assert pos == 0
    assert len(test_list) == 0

    pos_not_found = delete_logic(test_list, "Jon")
    assert pos_not_found == -1 
    assert len(test_list) == 0

def test_update_logic():
    test_list = [{"name": "Zak", "phone": "111", "age": "18", "email": "zak@uni"}]

    result = update_logic(test_list, "Zak", "Alex", "222", "19", "alex@uni")
    assert result == True
    assert len(test_list) == 1
    assert test_list[0]["name"] == "Alex"
    assert test_list[0]["phone"] == "222"