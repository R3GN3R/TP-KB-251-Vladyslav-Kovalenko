def find_new_position(sorted_list, new_element):
    for i in range(len(sorted_list)):
        if sorted_list[i] >= new_element:
            return i
    return len(sorted_list)
my_list =  [10, 20, 30, 40, 50]
new_value = 25

position = find_new_position(my_list, new_value)

print(f"Початковий відсортований список: {my_list}")
print(f"Елемент для вставки: {new_value}")
print(f"Знайдена позиція (індекс): {position}")

my_list.insert(position, new_value)
print(f"Список після вставки: {my_list}")